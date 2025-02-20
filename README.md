# Анализ покрытия кода

## Файл: NLog-5.2.7/src/NLog/Targets/NetworkLogEventDroppedEventArgs.cs
### Непокрытая строка: 1
Комментарий: Эта строка покрыта

```diff
-2 // Copyright (c) 2004-2021 Jaroslaw Kowalski <jaak@jkowalski.net>, Kim Christensen, Julian Verdurmen
-3 // 
-4 // All rights reserved.
-5 // 
-6 // Redistribution and use in source and binary forms, with or without 
-7 // modification, are permitted provided that the following conditions 
```

---
## Файл: NLog-5.2.7/src/NLog/Targets/ConsoleTarget.cs
### Непокрытая строка: 281
Комментарий: Эта строка покрыта

```diff
-275             {
-276                 RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-277                 if (targetBufferPosition > 0)
-278                 {
-279                     WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
-280                 }
-282         }
-283 
-284         private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
-285         {
-286             var output = GetOutput();
-287             using (var targetBuffer = _reusableEncodingBuffer.Allocate())
```

---
### Непокрытая строка: 282
Комментарий: Эта строка покрыта

```diff
-276                 RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-277                 if (targetBufferPosition > 0)
-278                 {
-279                     WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
-280                 }
-283 
-284         private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
-285         {
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
-289             {
-290                 int targetBufferPosition = 0;
-291                 try
-292                 {
-294                     {
-295                         targetBuilder.Result.ClearBuilder();
-296                         RenderLogEventToWriteBuffer(output, Layout, logEvents[i].LogEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
-297                         logEvents[i].Continuation(null);
-298                     }
-299                 }
```

---
## Файл: NLog-5.2.7/src/NLog/Targets/NetworkLogEventDroppedEventArgs.cs
### Непокрытая строка: 68
Комментарий: Эта строка покрыта

```diff
-62 
-63         /// <summary>
-64         /// The reason why log was dropped
-65         /// </summary>
-66         public NetworkLogEventDroppedReason Reason { get; }
-67     }
```

---
