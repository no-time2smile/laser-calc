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
android.archs = armeabi-v7a, arm64-v8a
android.ndk = 23b  
android.minapi = 21  
android.targetapi = 34
