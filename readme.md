# SPM *.sxm file to .png/.jpg file convertor
This tool aims to convert .sxm files to .png/.jpg(picture) files easily.
## usage

```python
import converter as cvt

# get a default configuration
cfg = cvt.Config.default()

# specify a target folder 
cfg.target_dir = "data/"
# specify a output folder
cfg.output_dir = "output/"

# convert it
cvt.Converter(cfg).convert_all()
```

You can randomly convert some files in the target folder (e.g. 1%):
```python
cfg.convert_percent = 0.01 
cvt.Converter(cfg).convert_randomly()
```

You can specify the output format by using:
```python
cfg.format = ".jpg"
```

You can also use multithreads to accelerate converting, but may encounter problems.
```python
cfg.threads = 5
```

by CoccaGuo
2020/12/05
