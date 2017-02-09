# Problem Authoring with Ubbr

The source code for an Ubbr is html with some embedded python code. The embedded python is placed between {% ubbr %} and {% endubbr %} tags. 

Example:

```
<h1> Ubbr source </h1> 

<p> Hello world! </p>
{% ubbr %}
import random
a = randint(10,100)
sum = 0
for i in range(1,a+1):
    sum += i

{% endubbr %}

<p> The sum of the integer 1,2 ... 
{% ubbr %}
echo(a)
{% endubbr %}

is {% ubbr %}
echo(sum)
{% endubbr %}
```

Some comments on the above snippet. If you are familiar with python, you will immediately wonder 'what is this echo(...) function?' It is a custom function that Ubbr adds to the global namespace that allows you to 'echo' content from your python code into the html output (just like the echo function in PHP). 

```
echo(x)
```

will insert some into the html in place of the {% ubbr %} .... {% endubbr %}
section where it occurs.

Apart from echo the rest of the code is just standard python code. 

A key point to note is that state is preserved across different ubbr sections within the same source code. In the example above, we define variables
``` a ``` and ```sum``` in the first section of python code. 
We can use these variables in later sections of python code.
    

