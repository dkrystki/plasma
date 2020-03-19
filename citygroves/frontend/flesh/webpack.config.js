'use strict';

const HtmlPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin');
const helpers = require('./helpers');

const {VueLoaderPlugin} = require('vue-loader');

module.exports = {
    mode: 'development',
    devtool: 'eval-source-map',
    entry: [
        `webpack-dev-server/client?http://0.0.0.0`,
        'webpack/hot/only-dev-server',
        './src/main.js'
    ],
    resolve: {
        extensions: ['.js', '.ts', '.vue'],
        alias: {
            'vue$': 'vue/dist/vue.runtime.js',
            '@': helpers.root('src'),
            '@components': helpers.root('src/components')
        }
    },
    output: {
        path: helpers.root('dist'),
        filename: 'js.bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.ts$/,
                use: [
                    {
                        loader: 'ts-loader',
                        options: {
                            transpileOnly: true
                        }
                    }
                ],
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                use: [
                    'vue-style-loader',
                    {loader: 'css-loader', options: {sourceMap: true}},
                ]
            },
            {
                test: /\.scss$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.sass$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    {
                        loader: 'sass-loader',
                        options: {
                            sassOptions: {
                                indentedSyntax: false
                            }
                        }
                    }
                ]
            },
            {
                test: /\.svg$/,
                use: [
                    'vue-svg-loader',
                ],
            },
            {
                test: /\.(png|jpe?g|gif|eot|woff2?|ttf)$/i,
                use: [
                    {
                        loader: 'file-loader',
                    },
                ],
            },
        ]
    },
    devServer: {
        compress: true,
        historyApiFallback: true,
        hot: true,
        open: true,
        overlay: true,
        host: '0.0.0.0',
        disableHostCheck: true,
        port: 80,
        stats: {
            normal: true
        }
    },
    plugins: [
        new VueLoaderPlugin(),
        new HtmlPlugin({
            template: 'index.html',
            chunksSortMode: 'dependency'
        }),
        new webpack.HotModuleReplacementPlugin(),
        new FriendlyErrorsPlugin()
    ]
};
