#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>

class Layer {
public:
    bool show;
    std::string name;
    int width;
    int height;
    int channels;
    cv::Mat image;
    cv::Mat mask;
    std::string mode;
    bool locked;

    Layer(bool show = true, std::string name = "Layer", int width = 0, int height = 0, int channels = 4)
        : show(show), name(name), width(width), height(height), channels(channels), locked(false)
    {
        image = cv::Mat::zeros(height, width, CV_8UC(channels));
        mask = cv::Mat::ones(height, width, CV_32F);
        mode = "Normal";
    }

    void drawRandomCircle()
    {
        int center_x = std::rand() % width;
        int center_y = std::rand() % height;
        int radius = std::rand() % (std::min(width, height) / 2 - 10) + 10;
        cv::Scalar color(std::rand() % 256, std::rand() % 256, std::rand() % 256, std::rand() % 256);

        cv::circle(image, cv::Point(center_x, center_y), radius, color, -1);
    }

    void resizeImage(int new_width, int new_height)
    {
        cv::resize(image, image, cv::Size(new_width, new_height));
    }

    void moveImage(int x, int y)
    {
        cv::Mat M = (cv::Mat_<double>(2, 3) << 1, 0, x, 0, 1, y);
        cv::warpAffine(image, image, M, image.size());
    }

    void applyMask()
    {
        cv::multiply(image, mask, image);
    }

    void rotateImage(double angle)
    {
        cv::Point2f center(image.cols / 2.0, image.rows / 2.0);
        cv::Mat rotation = cv::getRotationMatrix2D(center, angle, 1.0);
        cv::warpAffine(image, image, rotation, image.size());
    }
};

class Artboard {
public:
    int width;
    int height;
    std::vector<Layer> layers;
    int currentLayerIndex;

    Artboard() : width(800), height(800), currentLayerIndex(0)
    {
        initialize();
    }

    void initialize()
    {
        for (int i = 0; i < 10; ++i) {
            Layer layer(true, "Layer", width, height);
            layer.drawRandomCircle();
            layers.push_back(layer);
        }

        // Create checkerboard layer and set its properties
        Layer checkerboardLayer(true, "Checkerboard", width, height);
        createCheckerboard(checkerboardLayer.image);
        checkerboardLayer.locked = true;
        checkerboardLayer.image.convertTo(checkerboardLayer.image, CV_8UC4, 1.0, 0.1); // Set opacity to 10%
        // layers.insert(layers.begin(), checkerboardLayer);
    }

    void createCheckerboard(cv::Mat& image)
    {
        const int tileSize = 50;
        const int numTilesX = width / tileSize;
        const int numTilesY = height / tileSize;

        image.create(height, width, CV_8UC4);

        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                int tileX = j / tileSize;
                int tileY = i / tileSize;

                // Determine the color based on tile position
                uchar color = ((tileX + tileY) % 2 == 0) ? 255 : 200;

                image.at<cv::Vec4b>(i, j) = cv::Vec4b(color, color, color, 255);
            }
        }
    }

    cv::Mat compileLayers()
    {
        std::vector<Layer> layersToRender;
        for (const Layer& layer : layers) {
            if (layer.show)
                layersToRender.push_back(layer);
        }

        if (layersToRender.empty())
            return cv::Mat();

        cv::Mat compiledImage(height, width, CV_8UC4, cv::Scalar(0, 0, 0, 0));

        for (const Layer& layer : layersToRender) {
            cv::Mat layerImage = layer.image(cv::Rect(0, 0, width, height));
            cv::add(layerImage, compiledImage, compiledImage);
        }

        return compiledImage;
    }
};

int main()
{
    Artboard artboard;

    while (true) {
        cv::Mat compiledLayers = artboard.compileLayers();
        if (!compiledLayers.empty())
            cv::imshow("Artboard", compiledLayers);

        int key = cv::waitKey(0);
        if (key == 27) // ESC key to exit
            break;
        else if (key >= '0' && key <= '9') {
            int index = key - '0';
            if (index < artboard.layers.size())
                artboard.currentLayerIndex = index;
        }
        else if (key == 13) { // Enter key
            if (artboard.currentLayerIndex < artboard.layers.size()) {
                Layer& layer = artboard.layers[artboard.currentLayerIndex];
                layer.show = !layer.show;
            }
        }
        else if (key == 'l' || key == 'L') { // 'l' or 'L' key to lock/unlock the active layer
            if (artboard.currentLayerIndex < artboard.layers.size()) {
                Layer& layer = artboard.layers[artboard.currentLayerIndex];
                layer.locked = !layer.locked;
            }
        }
        else if (key == 0) { // Up arrow key
            Layer& layer = artboard.layers[artboard.currentLayerIndex];
            if (!layer.locked)
                layer.moveImage(0, -10);
        }
        else if (key == 1) { // Down arrow key
            Layer& layer = artboard.layers[artboard.currentLayerIndex];
            if (!layer.locked)
                layer.moveImage(0, 10);
        }
        else if (key == 2) { // Left arrow key
            Layer& layer = artboard.layers[artboard.currentLayerIndex];
            if (!layer.locked)
                layer.moveImage(-10, 0);
        }
        else if (key == 3) { // Right arrow key
            Layer& layer = artboard.layers[artboard.currentLayerIndex];
            if (!layer.locked)
                layer.moveImage(10, 0);
        }
        else if (key == 'r' || key == 'R') { // 'r' or 'R' key to rotate the active layer
            Layer& layer = artboard.layers[artboard.currentLayerIndex];
            if (!layer.locked)
                layer.rotateImage(45.0);
        }
    }

    cv::destroyAllWindows();

    return 0;
}
