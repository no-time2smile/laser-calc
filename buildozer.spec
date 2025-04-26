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

# Архитектуры (новый формат)
android.archs = armeabi-v7a, arm64-v8a

# Версии инструментов
android.ndk = 23b
android.sdk = 28
android.minapi = 21
android.targetapi = 28
