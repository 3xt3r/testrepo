# Анализ результатов, полученных при фаззинг-тестировании requests

## Анализ выявленных падений

На текущий момент при фаззинг-тестировании падений получено не было. 

## Анализ доcтигнутого покрытия

  - Целевая библиотека для фаззинг тестирования - [requests](https://github.com/psf/requests)
  - Целевой метод - requests.api.request
  - Целевой класс - HTTPBasicAuth
  - Фаззинг-скрипт, использованный при фаззинг-тестировании: fuzz_requests.py


### Целевой исходный код, непокрытый при фаззинг-тестировании

### Файл requests/api.py

Непокрытый код: стр. 73
```diff
62    0 :  def get(url, params=None, **kwargs):
63      :      r"""Sends a GET request.
64      :  
65      :      :param url: URL for the new :class:`Request` object.
66      :      :param params: (optional) Dictionary, list of tuples or bytes to send
67      :          in the query string for the :class:`Request`.
68      :      :param \*\*kwargs: Optional arguments that ``request`` takes.
69      :      :return: :class:`Response <Response>` object
70      :      :rtype: requests.Response
71      :      """
72      :  
-73      :      return request("get", url, params=params, **kwargs)
```

Непокрытый код: стр. 85
```diff
76    0 :  def options(url, **kwargs):
77      :      r"""Sends an OPTIONS request.
78      :  
79      :      :param url: URL for the new :class:`Request` object.
80      :      :param \*\*kwargs: Optional arguments that ``request`` takes.
81      :      :return: :class:`Response <Response>` object
82      :      :rtype: requests.Response
83      :      """
84      :  
-85      :      return request("options", url, **kwargs)
```

Непокрытый код: стр. 99-100
```diff
88    0 :  def head(url, **kwargs):
89      :      r"""Sends a HEAD request.
90      :  
91      :      :param url: URL for the new :class:`Request` object.
92      :      :param \*\*kwargs: Optional arguments that ``request`` takes. If
93      :          `allow_redirects` is not provided, it will be set to `False` (as
94      :          opposed to the default :meth:`request` behavior).
95      :      :return: :class:`Response <Response>` object
96      :      :rtype: requests.Response
97      :      """
98      :  
-99      :      kwargs.setdefault("allow_redirects", False)
-100     :      return request("head", url, **kwargs)
```

Непокрытый код: стр. 115
```diff
103   0 :  def post(url, data=None, json=None, **kwargs):
104     :      r"""Sends a POST request.
105     :  
106     :      :param url: URL for the new :class:`Request` object.
107     :      :param data: (optional) Dictionary, list of tuples, bytes, or file-like
108     :          object to send in the body of the :class:`Request`.
109     :      :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
110     :      :param \*\*kwargs: Optional arguments that ``request`` takes.
111     :      :return: :class:`Response <Response>` object
112     :      :rtype: requests.Response
113     :      """
114     :  
-115     :      return request("post", url, data=data, json=json, **kwargs)
```

Непокрытый код: стр. 130
```diff
118   0 :  def put(url, data=None, **kwargs):
119     :      r"""Sends a PUT request.
120     :  
121     :      :param url: URL for the new :class:`Request` object.
122     :      :param data: (optional) Dictionary, list of tuples, bytes, or file-like
123     :          object to send in the body of the :class:`Request`.
124     :      :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
125     :      :param \*\*kwargs: Optional arguments that ``request`` takes.
126     :      :return: :class:`Response <Response>` object
127     :      :rtype: requests.Response
128     :      """
129     :  
-130     :      return request("put", url, data=data, **kwargs)
```

Непокрытый код: стр. 145
```diff
133   0 :  def patch(url, data=None, **kwargs):
134     :      r"""Sends a PATCH request.
135     :  
136     :      :param url: URL for the new :class:`Request` object.
137     :      :param data: (optional) Dictionary, list of tuples, bytes, or file-like
138     :          object to send in the body of the :class:`Request`.
139     :      :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
140     :      :param \*\*kwargs: Optional arguments that ``request`` takes.
141     :      :return: :class:`Response <Response>` object
142     :      :rtype: requests.Response
143     :      """
144     :  
-145     :      return request("patch", url, data=data, **kwargs)
```

Непокрытый код: стр. 157
```diff
148   0 :  def delete(url, **kwargs):
149     :      r"""Sends a DELETE request.
150     :  
151     :      :param url: URL for the new :class:`Request` object.
152     :      :param \*\*kwargs: Optional arguments that ``request`` takes.
153     :      :return: :class:`Response <Response>` object
154     :      :rtype: requests.Response
155     :      """
156     :  
-157     :      return request("delete", url, **kwargs)
```
Комментарий: в данном модуле отсутствует покрытие для результатов возврата всех функций, которые в нем определены, кроме функции request.
Функции get, post, put, delete, head, options и patch из модуля requests.api являются обёртками вокруг основной функции request, фаззинг которой происходит в фаззинг-скрипте fuzz_requests.py. Поскольку в нем происходит вызов requests.request() с различными методами и параметрами, вышеперечисленные функции не вызываются в коде напрямую. Поскольку методы являются обертками над request, и их отличие между собой только в строковом значении указываемого HTTP-метода, отдельный фаззинг не требуется.

### Файл requests/sessions.py

Целевой метод requests.api.request является оберткой над функцией requests.sessions.Session.request, которая покрывается вся. 
Далее функция requests.sessions.Session.request вызывает следующие функции, которые потенциально попадают на поверхность атаки:
 - requests.models.Request
 - requests.sessions.Session.prepare_request
 - requests.sessions.Session.merge_environment_settings
 - requests.sessions.Session.send

### requests.sessions.Session.prepare_request

```diff
470   0 :          if not isinstance(cookies, cookielib.CookieJar):
-471     :              cookies = cookiejar_from_dict(cookies)
472     :  
473     :          # Merge with session cookies
474     :          merged_cookies = merge_cookies(
475     :              merge_cookies(RequestsCookieJar(), self.cookies), cookies
476     :          )
477     :  
478     :          # Set environment's basic authentication if not explicitly set.
479     :          auth = request.auth
480     :          if self.trust_env and not auth and not self.auth:
-481     :              auth = get_netrc_auth(request.url)
482     :  
483     :          p = PreparedRequest()
484     :          p.prepare(
485     :              method=request.method.upper(),
486     :              url=request.url,
487     :              files=request.files,
488     :              data=request.data,
489     :              json=request.json,
490     :              headers=merge_setting(
491     :                  request.headers, self.headers, dict_class=CaseInsensitiveDict
492     :              ),
493     :              params=merge_setting(request.params, self.params),
494     :              auth=merge_setting(auth, self.auth),
495     :              cookies=merged_cookies,
496     :              hooks=merge_hooks(request.hooks, self.hooks),
497     :          )
498     :          return p
```
Комментарий: не покрывается строка 471, 
Также не покрывается строка 481, относящаяся к логике аутентификации. Функция пытается получить логин и пароль из файла .netrc. Если для request.url найдена запись, возвращается (username, password). Если файл .netrc отсутствует или нет записи для url, возвращает None. 
В функционале основного ПО, в котором используется модуль requests, отсутствует обращение к модулю аутентификации, следовательно покрытие данного кода на текущий момент не требуется. 


### requests.sessions.Session.merge_environment_settings

```diff
757     :          if self.trust_env:
758     :              # Set environment's proxies.
759     :              no_proxy = proxies.get("no_proxy") if proxies is not None else None
760     :              env_proxies = get_environ_proxies(url, no_proxy=no_proxy)
761     :              for k, v in env_proxies.items():
-762     :                  proxies.setdefault(k, v)
763     :  
```
Комментарий: в функции merge_environment_settings не покрывается строка 762, которая участвует в установке прокси-серверов на основе настроек системы. Это часть прокси-режима в requests, который позволяет автоматически применять системные прокси или прокси, указанные пользователем. В функционале основного ПО, в котором используется модуль requests, данная настройка не участвует. 

### requests.sessions.Session.send

```diff
688     :          if isinstance(request, Request):
-689     :              raise ValueError("You can only send PreparedRequests.")
690     :  
691     :          # Set up variables needed for resolve_redirects and dispatching of hooks
692     :          allow_redirects = kwargs.pop("allow_redirects", True)
693     :          stream = kwargs.get("stream")
694     :          hooks = request.hooks
695     :  
696     :          # Get the appropriate adapter to use
697     :          adapter = self.get_adapter(url=request.url)
698     :  
699     :          # Start time (approximately) of the request
700     :          start = preferred_clock()
701     :  
702     :          # Send the request
703     :          r = adapter.send(request, **kwargs)
704     :  
705     :          # Total elapsed time of the request (approximately)
706     :          elapsed = preferred_clock() - start
707     :          r.elapsed = timedelta(seconds=elapsed)
708     :  
709     :          # Response manipulation hooks
710     :          r = dispatch_hook("response", hooks, r, **kwargs)
711     :  
712     :          # Persist cookies
713     :          if r.history:
714     :              # If the hooks create history then we want those cookies too
-715     :              for resp in r.history:
-716     :                  extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
717     :  
718     :          extract_cookies_to_jar(self.cookies, request, r.raw)
719     :  
720     :          # Resolve redirects if allowed.
721     :          if allow_redirects:
722     :              # Redirect resolving generator.
723     :              gen = self.resolve_redirects(r, request, **kwargs)
724     :              history = [resp for resp in gen]
725     :          else:
726     :              history = []
727     :  
728     :          # Shuffle things around if there's history.
729     :          if history:
730     :              # Insert the first (original) request at the start
-731     :              history.insert(0, r)
732     :              # Get the last request made
-733     :              r = history.pop()
-734     :              r.history = history
```
Комментарий: код на стр. 689 является обработкой исключения ValueError, не требуется фаззить. Код на стр. 715-716 относится к обработке редиректов, механизм перенаправления не используется в функционале основного ПО, в котором используется модуль requests.
Код на стр. 731-734 также относится к обработке редиректов. 

### Файл requests/models.py

### requests.models.Request

```diff
-280    :              self.register_hook(event=k, hook=v)
281     :  
282     :          self.method = method
283     :          self.url = url
284     :          self.headers = headers
285     :          self.files = files
286     :          self.data = data
287     :          self.json = json
288     :          self.params = params
289     :          self.auth = auth
290     :          self.cookies = cookies
291     :  
292     :      def __repr__(self):
-293     :          return f"<Request [{self.method}]>"
```
Комментарий: в стр. 280 код выполняет регистрацию пользовательских хуков (hooks) в объекте запроса. Пользовательские хуки не используются в функционале основного ПО, в котором используется модуль requests.
В стр. 293 метод __repr__ определяет текстовое представление объекта и используется в Python для отладки и логирования, которые не используются в функционале основного ПО, в котором используется модуль requests. 

### Файл requests/auth.py      

### requests.auth.HTTPBasicAuth

```diff
76      :  class HTTPBasicAuth(AuthBase):
77      :      """Attaches HTTP Basic Authentication to the given Request object."""
78      :  
79      :      def __init__(self, username, password):
80      :          self.username = username
81      :          self.password = password
82      :  
83      :      def __eq__(self, other):
-84      :          return all(
85      :              [
86      :                  self.username == getattr(other, "username", None),
87      :                  self.password == getattr(other, "password", None),
88      :              ]
89      :          )
90      :  
91      :      def __ne__(self, other):
-92      :          return not self == other
93      :  
94      :      def __call__(self, r):
95      :          r.headers["Authorization"] = _basic_auth_str(self.username, self.password)
96      :          return r
```
Комментарий: метод __eq__ отвечает за проверку равенства двух объектов. В данном случае метод определяет, равны ли два объекта, сравнивая атрибуты username и password. Метод __eq__ не покрывается фаззингом, потому что не проверяются сценарии, где вызывается оператор == между двумя объектами. Поскольку метод реализует простое сравнение двух строк, фаззинг здесь не требуется.
Метод __ne__ отвечает за проверку неравенства объектов (вызывается, когда используется оператор !=). Метод __ne__ не покрывается фаззингом из-за отсутствия проверок с использованием оператора !=. Поскольку метод реализует простое сравнение двух строк, фаззинг здесь не требуется.

### requests.auth._basic_auth_str

```diff
25    0 :  def _basic_auth_str(username, password):
26      :      """Returns a Basic Auth string."""
27      :  
28      :      # "I want us to put a big-ol' comment on top of it that
29      :      # says that this behaviour is dumb but we need to preserve
30      :      # it because people are relying on it."
31      :      #    - Lukasa
32      :      #
33      :      # These are here solely to maintain backwards compatibility
34      :      # for things like ints. This will be removed in 3.0.0.
35      :      if not isinstance(username, basestring):
-36      :          warnings.warn(
37      :              "Non-string usernames will no longer be supported in Requests "
38      :              "3.0.0. Please convert the object you've passed in ({!r}) to "
39      :              "a string or bytes object in the near future to avoid "
40      :              "problems.".format(username),
41      :              category=DeprecationWarning,
42      :          )
-43      :          username = str(username)
44      :  
45      :      if not isinstance(password, basestring):
-46      :          warnings.warn(
47      :              "Non-string passwords will no longer be supported in Requests "
48      :              "3.0.0. Please convert the object you've passed in ({!r}) to "
49      :              "a string or bytes object in the near future to avoid "
50      :              "problems.".format(type(password)),
51      :              category=DeprecationWarning,
52      :          )
-53      :          password = str(password)
54      :      # -- End Removal --
55      :  
56      :      if isinstance(username, str):
```
Комментарий: в данном случае код не покрывается в стр. 36, 43, 46, 53, так как warnings.warn() в этом коде используется для обработки некорректных данных для username и password, которые и так генерируются фаззером. 
