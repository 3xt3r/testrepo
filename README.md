# Анализ покрытия кода

## Файл: src/NLog/Targets/ConsoleTarget.cs
### Непокрытая строка: 293
Комментарий: Эта строка покрыта

```diff
- 293:             using (var targetBuffer = _reusableEncodingBuffer.Allocate())
            using (var targetBuilder = ReusableLayoutBuilder.Allocate())
            {
                int targetBufferPosition = 0;
                try
                {
                    for (int i = 0; i < logEvents.Count; ++i)
                    {
                        targetBuilder.Result.ClearBuilder();
                        RenderLogEventToWriteBuffer(output, Layout, logEvents[i].LogEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
                        logEvents[i].Continuation(null);
                    }
                }
```

---
### Непокрытая строка: 282
Комментарий: Эта строка покрыта

```diff
- 282:                 RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
                if (targetBufferPosition > 0)
                {
                    WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
                }
            }
        }

        private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
        {
            var output = GetOutput();
            using (var targetBuffer = _reusableEncodingBuffer.Allocate())
            using (var targetBuilder = ReusableLayoutBuilder.Allocate())
```

---
### Непокрытая строка: 281
Комментарий: Эта строка покрыта

```diff
- 281:             {
                RenderLogEventToWriteBuffer(output, layout, logEvent, targetBuilder.Result, targetBuffer.Result, ref targetBufferPosition);
                if (targetBufferPosition > 0)
                {
                    WriteBufferToOutput(output, targetBuffer.Result, targetBufferPosition);
                }
            }
        }

        private void WriteBufferToOutput(IList<AsyncLogEventInfo> logEvents)
        {
            var output = GetOutput();
            using (var targetBuffer = _reusableEncodingBuffer.Allocate())
```

---
