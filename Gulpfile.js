var gulp = require('gulp'),
    sass = require('gulp-sass'),
    neat = require('node-neat').includePaths,
    watch = require('gulp-watch');

gulp.task('sass', function() {
  return gulp.src('scss/*.scss')
    .pipe(sass({
      includePaths: ['styles'].concat(neat)
    }))
    .pipe(gulp.dest('css'))
});

gulp.task('watch', function() {
  gulp.watch('scss/*.scss', ['sass']);
});

gulp.task('default', ['sass', 'watch']);
