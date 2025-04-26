[app]
title = Laser Calc
package.name = lasercalc
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0,numpy
orientation = portrait
fullscreen = 0

# Актуальные параметры Android
android.archs = armeabi-v7a, arm64-v8a  # Поддержка ARM архитектур
android.ndk = 23b  # Версия NDK
android.minapi = 21  # Минимальная версия Android (5.0 Lollipop)
android.targetapi = 34  # Целевая версия Android (актуальная)
