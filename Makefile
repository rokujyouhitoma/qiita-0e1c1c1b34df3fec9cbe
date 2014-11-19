RM := rm -rf

build: clean
	python setup.py build_ext --inplace

.PHONY: clean
clean:
	$(RM) *.so build