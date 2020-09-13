如何用equests下载图片

```python
if r.status_code == 200:
	open(path,'wb').write(r.content)
del r
```

