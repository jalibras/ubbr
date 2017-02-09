
Assuming that the ubbr root directory is in the python path try 


```python
from ubbr.engine.core import Ubbr
```


```python
u = Ubbr('Hello world!')
```


```python
u.get_template()
```




    'Hello world!'



Anything between {% ubbr %} and {% endubbr %} tags is treated as executable Python code 


```python
v = Ubbr('Hello {% ubbr %} a = 1 \nprint(a){% endubbr %}')
```

The python code must, of course, be properly indented. Try inserting a space after \n in the above source string


```python
v.get_template()
```




    'Hello {{ ubbrvalues.0 }}'



Observe that in the template output the {% ubbr %} ... {% endubbr %} section has been replaced by {{ ubbervalues.0 }} which a conventional syntax for html template variable interpolation. Thus we can use the output of Ubbr.template as a template in web application frameowrks like Django/Flask. Where do we get the ubbervalues variable?


```python
v.get_context()
```

    1





    ([''], [])



The first entry in this pair is the value of ubbrvalues. This is not a very interesting example


```python
w = Ubbr('Hello {% ubbr %} echo(" world!"){% endubbr%}')
w.get_template()
```




    'Hello {{ ubbrvalues.0 }}'




```python
w.get_context()
```




    ([' world!'], [])



So the basic useage pattern in a web app is ...

Create an Ubbr instance and get the source from somewhere e.g. database

```
u = Ubbr([source])
```

generate a template with 
```
template = u.get_template()
```

generate the value of the ubbrvalues context variable
```
ubbrvalues = u.get_context()[0]
```

render the template and serve using whatever framework you are using


```python

```
