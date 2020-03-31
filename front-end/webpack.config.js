const path = require('path');
const webpack = require('webpack');
const htmlWebpackPlugin = require('html-webpack-plugin');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');


module.exports = {
    entry: {
        index: './src/main.js'
    },
    output: {
        // publicPath: path.resolve(__dirname ),
        path: path.resolve(__dirname, 'dist'),
        filename: "[name].[hash].js"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: [
                    {
                        loader: "babel-loader",
                        options: {
                            presets: ["@babel/preset-env"]
                        }
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            hmr: process.env.NODE_ENV === 'development',
                        },
                    },
                    // {loader: "style-loader"},
                    {loader: "css-loader"},
                    {loader: "postcss-loader"}
                ],
                include: path.resolve(__dirname, 'src'),
                exclude: /node_modules/
            },
            {
                test: /.scss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            hmr: process.env.NODE_ENV === 'development',
                        },
                    },
                    // {loader: "style-loader"},
                    {loader: "css-loader"},
                    {loader: "sass-loader"}
                ]
            },
            {
                test: /\.(png|jpg|jpeg|gif|svg)/,
                use: {
                    loader: "url-loader", options: {
                        outputPath: 'images/',
                        limit:5*1024
                    }
                }
            }
        ]
    },
    optimization: {
        minimizer: [new UglifyJSPlugin()]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            filename: '[name].css'
        }),
        new htmlWebpackPlugin(
            {
                filename: "index.html",
                template: "./index.html",
                hash: true
            }
        ),
        new webpack.ProvidePlugin({
            axios: 'axios'
        }),
        new webpack.DefinePlugin(
            {
                NODE_ENV:JSON.stringify(process.env.NODE_ENV)
            }
        )
    ],
    // devServer: {
    //     content: path.resolve(__dirname, 'dist'),
    //     port: 9000,
    //     host: '0.0.0.0',
    //     hot: true,
    //     useLocalIp: true,
    //     open: true,
    //     compress: true
    // }
};
