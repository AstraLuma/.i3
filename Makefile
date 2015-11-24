config: config.d/*
	cat config.d/* > config
	i3-msg reload

install: config
	ln -fs $(realpath xsession) ~/.xsession
	mkdir -p ~/.config/dunst
	ln -fs $(realpath dunstrc) ~/.config/dunst/dunstrc