# Postmortem
![https://api.whatsapp.com/send?phone=3185040951&text=hola%20bro!%20quiero%20saber%20mas%20de%20ti!](https://www.idento.es/wp-content/uploads/2014/10/10-errores-tipicos-diseno-desarrollo-web.jpg)

## Issue Summary:
---
On 1/02/21 at 2:23 pm PST, 100% of the website's service was down for a total 12 minutes, with service reinstated at 2:35 pm PST. Users universally experienced a response with a status code of 500 (internal server error). The main cause of the interrupt was a single character typo in which a .py file was written as .py with a trailing space.

## Timeline for 1/02/21 (PST):

---
* 2:23 pm: After deploying a Flask update, a junior engineer noticed that the website was returning a 500 status code.

* 2:25 pm: All running processes on a particular server were checked using `ps auxf`. Nginx and MySQL were found to be running as expected, indicating an error with PYTHON/Flask.

* 2:26 pm: The Nginx configuration file `/etc/nginx/sites-enabled/default` was edited to enable debug mode.

* 2:27 pm: The website was curled to reveal a fatal error, a missing file `/var/www/html/index.py_ ` ("_" = represents the white space) required in `/var/www/html/index.py`. The nonexistent .py" ", extension indicated a potential typographical error.

* 2:28 pm: ls was used to check the contents of `/var/www/html/`. It was discovered that the file `/var/www/html/index.py_ ` ("_" = represents the white space) existed, confirming a typographical error was made.

* 2:30 pm: The typographical error was fixed on the individual server using sed -i `'s/py_/py/'` `/var/www/html/index.py`.

* 2:31 pm: Website service was then tested once more, with content being served as expected.

* 2:32 pm: A puppet manifest was developed to fix this issue on a large scale.

* 2:35 pm: The puppet manifest was deployed on all remaining servers, bringing website service back to 100%.

## Root cause and resolution:

---

The root cause of this outage was a typo made in the python file `/var/www/html/` in which the file `/var/www/html/index.py` was required. The extension of `.py` was a typographical error, meant to be .py_ . Since `/var/www/html/index.py_ ` ("_" = represents the white space) did not exist and was required, a fatal error was raised, preventing content from being served. Since this code was deployed on all servers, this error caused a 100% outage. A puppet manifest to fix the typographical error was developed and deployed on all servers, reinstating service within 12 minutes of the outage.


## Corrective and preventative measures:

---
To prevent wide-scale issues like this from occurring in the future, code should never be deployed on all servers before testing. Some things to consider for the future are: 
- the development of company-wide testing protocol
- setting up isolated docker containers for testing purposes 
- and the implementation of a two-person sign-off before major deployment.

## Author
---
- **GitHub**[@ronald0204](https://github.com/ronald0204)
- **Twiitter:** [@ronald45251997](https://twitter.com/ronald45251997)
