# Kobe-Engineer-Crawler
A Python Crawler Implement for Kobe-Engineer(靠北工程師)

## What is Kobe-Engineer?

**Kobe-Engineer** is Facebook fans page where providing engineers to give vent to complain about the job, work, co-worker, **PM**, boss, and anything.

The most interesting of **Kobe-Engineer** is its **publisher system**.

It allows user publish post anonymously, and the post can be transferred to picture automatically.

You can check [**Kobe-Engineer**](https://www.facebook.com/kobeengineer/) and its [**publisher system**](https://engineer.kobe.ga/).

You can also find the [**source code**](https://github.com/kxgen/facebook-anonymous-publisher) of publisher system.

## Requirement

**Kobe-Engineer-Crawler** is built by **Python 3** and only using **requests** library to crawling data.

Make sure you already have **requests**, or you can use pip to instal them.
```s
pip install requests
```

## How to Use?

**Kobe-Engineer-Crawler** have to set **token** to communicate to **Facebook graph API**.

So, go to [Facebook for developers](https://developers.facebook.com/) -> tools & support, and you can find **Graph API Explorer** at Tools.

It will provide **token** to test **Facebook graph API**.

Just use it in this crawler.

After setting of **token**, you have to setting how much posts you want crawling.

Then, you can run this crawler in terminal.

```$
python Kobe-Engineer-Crawler.py
```
