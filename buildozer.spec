[app]
# (str) Title of your application
title = Nutri Search

# (str) Package name
package.name = Nutri_search

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy
requirements = python3,kivy,requests

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use (if empty, it will be automatically selected)
# android.ndk = 21b

# (bool) Enable Android logcat during build
logcat = 1

# (bool) Android logcat only display log for the specified application
logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (list) The Android archs to build for (one of armeabi-v7a, arm64-v8a, x86, x86_64)
# In most cases, only the first arch will be built.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable Android APK expansion (if the APK is over 50MB, it's a requirement)
# android.expansion = False

# (list) patterns to include into the build
#source.include_patterns = assets/*,images/*.png

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (str) Android Additional AAR dependencies
#android.add_aars =

# (str) Android Additional Java dependencies
#android.add_jars =

# (str) Android Additional libraries
#android.add_libs =

# (str) Android Additional manifest xml
#android.add_manifest_xml =

# (str) Android Additional build gradle
#android.add_build_gradle =

# (str) Android Additional proguard rules
#android.add_proguard_rules =

# (str) Android Additional services
#android.add_services =

# (str) Android Additional permissions
#android.add_permissions =

# (str) Android Main Java Class
#android.main_java_class =

# (str) Android manifest activity class
#android.manifest_activity_class =

# (str) Android manifest service class
#android.manifest_service_class =

# (str) Android project build gradle classpath
#android.project_build_gradle_classpath =

# (str) Android project repositories
#android.project_repositories =

# (str) Android build gradle
#android.build_gradle =

# (str) Android gradle dependencies
#android.gradle_dependencies =

# (str) Android gradle plugins
#android.gradle_plugins =

# (str) Android manifest queries
#android.manifest_queries =

# (str) Android JVM arguments
#android.jvm_args =

# (str) Android Lint options
#android.lint_options =

# (str) Additional presplash animation options (if presplash.filename is not empty)
# presplash.animation =

# (list) comma separated e.g. sqlite3,kivy_garden
#osx.python_use_target_python = 1

# (bool) Enable custom build script
# p4a.custom_build =

# (str) Custom build script to use
# p4a.custom_build_script =

# (str) Custom recipe list
# p4a.custom_recipes =

# (list) List of gradle plugins to add to the android build
#android.add_gradle_plugins =

# (str) Custom repository url
#android.repository_url =

# (str) Custom gradle properties
#android.gradle_properties =

# (str) Buildozer package data for debug
#package_data =
