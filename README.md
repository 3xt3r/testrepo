# Анализ покрытия кода

## Файл: src/NLog/Targets/ConsoleTarget.cs
### Непокрытая строка: 281
Комментарий: Эта строка покрыта

```diff
 275             {
-276                 RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-277                 if (targetBufferPosition > 0)
 278                 {
-279                     WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
 280                 }
-281             }
-282         }
 283 
 284         private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
 285         {
-286             var output = GetOutput();
-287             using (var targetBuffer = _reusableEncodingBuffer.Allocate())
```

---
### Непокрытая строка: 282
Комментарий: Эта строка покрыта

```diff
-276                 RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-277                 if (targetBufferPosition > 0)
 278                 {
-279                     WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
 280                 }
-281             }
-282         }
 283 
 284         private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
 285         {
-286             var output = GetOutput();
-287             using (var targetBuffer = _reusableEncodingBuffer.Allocate())
-288             using (var targetBuilder = ReusableLayoutBuilder.Allocate())
```

---
### Непокрытая строка: 293
Комментарий: Эта строка покрыта

```diff
-287             using (var targetBuffer = _reusableEncodingBuffer.Allocate())
-288             using (var targetBuilder = ReusableLayoutBuilder.Allocate())
 289             {
-290                 int targetBufferPosition = 0;
 291                 try
 292                 {
-293                     for (int i = 0; i < logEvents.Count; ++i)
 294                     {
-295                         targetBuilder.Result.ClearBuilder();
-296                         RenderLogEventToWriteBuffer(output, Layout, logEvents[i].LogEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-297                         logEvents[i].Continuation(null);
 298                     }
-299                 }
```

---
## Файл: src/NLog/Targets/NetworkLogEventDroppedEventArgs.cs
### Непокрытая строка: 1
Комментарий: Эта строка покрыта

```diff
 1 // 
 2 // Copyright (c) 2004-2021 Jaroslaw Kowalski <jaak@jkowalski.net>, Kim Christensen, Julian Verdurmen
 3 // 
 4 // All rights reserved.
 5 // 
 6 // Redistribution and use in source and binary forms, with or without 
 7 // modification, are permitted provided that the following conditions 
```

---
