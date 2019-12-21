'use strict';

const HtmlPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin');
const helpers = require('./helpers');

const {VueLoaderPlugin} = require('vue-loader');

module.exports = {
    mode: 'development',
    entry: [
        './src/main.js'
    ],
    resolve: {
        extensions: ['.js', '.vue'],
        alias: {
            'vue$': 'vue/dist/vue.runtime.js',
            '@': helpers.root('src')
        }
    },
    output: {
        path: helpers.root('dist'),
        publicPath: '/',
        filename: 'js/[name].bundle.js',
        chunkFilename: 'js/[id].chunk.js'
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.pug$/,
                loader: 'pug-plain-loader'
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
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
                                indentedSyntax: true
                            }
                        }
                    }
                ]
            },
            {
                test: /\.svg$/,
                use: [
                    'babel-loader',
                    'vue-svg-loader',
                ],
            },
            {
                test: /\.(png|jpe?g|gif)$/i,
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
        port: 8000,
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
