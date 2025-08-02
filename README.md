# yashaslokesh.github.io

## packages

Add new packages with `uv add {package}`

- `uv run pelican-plugins` to discover all namespace plugins in the environment
- `uv run pelican-themes` 

## Development


Do all devlopment on the `source` branch. The `master` branch is for 
the static website assets

To make a new post, you can use 
```shell
python create_new_post.py -t title -c category
```

- **make devserver** to test changes
- git commit
- make