- Don't use public url shortening API'S
- Use MongoDB using Atlas
- Link should be directed based on platform(ios, android, desktop)
- No user auth
- Implement the API as documented below
- MVC, separate logic form representation,
- git commit log is required write good commit log
- Deplaoy on digital Ocean, Postman file


API 
- 

Bonus
- unittest
- one page screen for smart links generation
- Implementing user authentication is a bonus (basicAuth or OAuth2)
```
{
  "slug": "s5G1f3",
  "ios": {
    "primary": "http://...",
    "fallback": "http://..."
  },
  "android": {
    "primary": "http://...",
    "fallback": "http://..."
  },
  "web": "http://..."
}

{
  "slug": "s5G1f3",
  "ios": {
    "primary": "http://...",
    "fallback": "http://..."
  },
  "android": {
    "primary": "http://...",
    "fallback": "http://..."
  },
  "web": "http://..."
}
```