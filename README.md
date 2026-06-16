# sistema-bolao-copa
Sistema criado em Django para a realização do bolão da copa de 2026


## Estrutura

```bash

core/
│
├── settings.py
├── urls.py
└── templates/

campeonato/
│
├── models.py
│   ├── Time
│   ├── DiaJogo
│   ├── Jogo
│   └── Configuracao
│
├── admin.py
├── views.py
└── services.py

palpites/
│
├── models.py
│   └── Palpite
│
├── views.py
├── services.py
├── ranking.py
└── forms.py



```
