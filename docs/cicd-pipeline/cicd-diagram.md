## Pipeline Diagram
 
```
Push to main (trigger)
        │
        ▼
   ┌─────────┐
   │  Test   │  ← unit + integration tests
   └────┬────┘
        │ pass
        ▼
   ┌─────────┐
   │  Build  │  ← compile, package artifact
   └────┬────┘
        │ pass
        ▼
   ┌─────────┐
   │ Deploy  │  ← push via env secrets
   └────┬────┘
        │
        ▼
   ┌──────────────┐
   │  Smoke Test  │  ← GET / → expect 200
   └──┬───────┬───┘
      │       │
   pass      fail
      │       │
  Pipeline  Alert +
  complete  rollback
```
