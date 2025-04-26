[app]
title = Laser Calc
package.name = lasercalc
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
[app]
source.include_patterns = *.py,*.png,*.jpg,*.kv
requirements = python3, kivy==2.1.0, numpy  # numpy часто требуется для расчетов
android.arch = armeabi-v7a  # архитектура ARM
version = 1.0
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.0.0
fullscreen = 0
