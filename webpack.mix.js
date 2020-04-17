const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.setPublicPath('static');

mix.sass('resources/sass/app.scss', 'static/css/app.css')
    .js([
        'resources/js/before.js',
        'resources/js/app.js',
        'resources/js/after.js'
    ], 'static/js/app.js')
    .extract([
        'jquery',
        'bootstrap',
        'popper.js/dist/umd/popper'
    ])
    .sourceMaps();

/* Options */
mix.options({
    processCssUrls: true
});


if (mix.inProduction() || process.env.npm_lifecycle_event !== 'hot') {
    mix.version();
}
