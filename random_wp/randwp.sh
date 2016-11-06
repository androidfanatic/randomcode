# NSFW warning - do not use at work
# Downloads random wallpaper from wallheaven.cc

rnd="wallhaven-$RANDOM.jpg"
url="https://wallpapers.wallhaven.cc/wallpapers/full/"$rnd
path="file://"`pwd`/$rnd
wget $url
gsettings set org.gnome.desktop.background picture-uri $path
