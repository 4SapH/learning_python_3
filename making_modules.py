import making_modules_example

making_modules_example.ex('test')


'''
modules can be put
  in python\site-packages
    ---> acts globally
    ---> can be accessed from any script

    # my site-packages:
    C:\Users\Sergiu\AppData\Local\Programs\Python\Python36-32\Lib\site-packages
    ---> to find:
        py
        import site
        site.getsitepackages()[0]
    ---> OR on linux:
        which python3
        (usually: usr/lib/python3.5)

  in same folder
    ---> locally

'''
