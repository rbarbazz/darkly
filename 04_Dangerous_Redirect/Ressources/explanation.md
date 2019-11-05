On: ```/```

### Flaw
Change the site query parameter on any of the socials links.

ex: ```http://10.13.0.216/index.php?page=redirect&site=badsite```

Can be used in case of phishing, the base url looks legit. The user then thinks that he is going to a legit website(online banking for instance) but is redirected to a malicious website.
