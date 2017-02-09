# Problem Authoring with Ubbr

The source code for an Ubbr is html with some embedded python code. The embedded python is placed between {% ubbr %} and {% endubbr %} example. 

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



    

