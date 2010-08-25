default: all

all:
	cd bind; python setup.py build_ext -f -b ../

clean:
	rm -rf *.so
