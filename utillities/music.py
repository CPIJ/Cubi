music = {
    "power_on": [ 'C5s', 'C6s' ],
    "power_off": [ 'C6s', 'C5s' ],
    "wrong": [ 'C2h' ],
    "right": [ 'C5h' ],
    "mode_change": [ 'C6s', 'rs', 'C6s' ]
}


def get_music(name):
	song = music.get(name)

	if not song:
		raise ValueError('Unkown song: ' + name)

	return song
