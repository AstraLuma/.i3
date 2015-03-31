config: config.d/*
	cat config.d/* > config
	i3-msg reload
