# Problem Authoring with Ubbr

## Setting up the sample web application 

The sample web app is a bare bones Django application that is meant 
to demonstrate some very basic usage patterns. It can also 
be used by problem authors to try out problem code snippets.

To get it up and running on localhost

1. Install Django for your version of python. It has been tested with Python 3.5 and Django 1.10. It should woWith other versions of Python and Django but YMMV.

2. Deploy the application on a test server. In a linux environment, the following shell commands will do that

$ cd ubbr_webapp

$ python manage.py runserver


Now open a broswer and go to localhost:8000/admin and you should 
see the Django admin login page. Login with 
username: admin and password: ubbr1234

Now click on Model ubbrs and you will see a list of sample ubbr sources. Click on one to inspect/edit the source code. On the edit page for the source code you will also see a view on site link towards the top right - this allows you to see the rendered problem in your browser. Don't forget to save any changes before you view.

You can create a new problem by clicking on the ADD MODEL UBBR link from the model ubbr list view page. Enter the source code and save. To view the rendered problem, use the "view on site" link from the source code edit page as above. 




## A first example

The source code for an Ubbr is html with some embedded python code. The embedded python is placed between {% ubbr %} and {% endubbr %} tags. 

Example:

```
<h1> Ubbr source example</h1> 

<p> Hello world! </p>
{% ubbr %}
import random
a = random.randint(10,100)
sum = 0
for i in range(1,a+1):
    sum += i

{% endubbr %}

<p> The sum of the integers 1,2 ..., 
{% ubbr %}
echo(a)
{% endubbr %}

is {% ubbr %}
echo(sum)
{% endubbr %}
```

When this snippet is passed to the Ubbr engine and compiled, it produces the following html output 

```
<h1> Ubbr source example</h1> 

<p> Hello world! </p>


<p> The sum of the integers 1,2 ..., 
88

is 3916
```


Some comments on the above snippet. 

If we run this more than once we will see different outputs since the call to ```random.randint``` will produce different results each time. Later we will see how to pass a seed to the RNG so that we can obtain repeatable results if necessary.

If you are familiar with python, you will immediately wonder 'what is this echo(...) function?' It is a custom function that Ubbr adds to the global namespace that allows you to 'echo' content from your python code into the html output (just like the echo function in PHP). 

```
echo(x)
```

will insert some into the html in place of the {% ubbr %} .... {% endubbr %}
section where it occurs.

Apart from echo the rest of the code is just standard python code. 

A key point to note is that state is preserved across different ubbr sections within the same source code. In the example above, we define variables
``` a ``` and ```sum``` in the first section of python code. 
We can use these variables in later sections of python code.
    
A second important point to remember is that whitespace is syntactic in 
Python. In other words any python code inside the ubbr tags must 
be properly indented just like any other python code. On the other hand, 
whitespace outside the ubbr tags is treated like whitespace in any normal html code. 
