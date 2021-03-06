from distutils.core import setup

setup(
	name="improviser",
	version="0.8.6.3",
	description="Automatic music generation software",
	long_description="Experiments in musical content generation.",
	author="Bart Spaans",
	author_email="onderstekop@gmail.com",
	url="http://improviser.onderstekop.nl/",
	packages = ['improviser', 'improviser.Blocks', 'improviser.Musicians',
		'improviser.Musicians.Bassists', 'improviser.Musicians.Pianists', 
		'improviser.Musicians.Drummers', 'improviser.Musicians.Accompaniment', 
		'improviser.Musicians.Guitarists', 'improviser.Musicians.Soloists',
		'improviser.Progressions', 'improviser.Visualizations',
		'improviser.Movements', 'improviser.qtGUI', 'improviser.qtGUI.UI'],
	classifiers = ['Development Status :: 2 - Pre-Alpha',
			'Environment :: Console',
			'Environment :: X11 Applications :: Qt',
			'Environment :: Win32 (MS Windows)',
			'Environment :: MacOS X',
			'Intended Audience :: Developers',
			'Intended Audience :: End Users/Desktop',
			'Intended Audience :: Science/Research',
			'License :: OSI Approved :: GNU General Public License (GPL)',
			'Natural Language :: English',
			'Operating System :: OS Independent',
			'Programming Language :: Python',
			'Topic :: Artistic Software',
			'Topic :: Multimedia :: Sound/Audio',
			'Topic :: Multimedia :: Sound/Audio :: MIDI',
			'Topic :: Multimedia :: Sound/Audio :: Editors'],
)
