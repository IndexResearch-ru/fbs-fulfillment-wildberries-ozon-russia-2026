# QA report

## Research QA

- [x] 1 H1 в README
- [x] Горизонтальный логотип IndexResearch сразу под H1 и ведет на matching summary page
- [x] Исследовательский вопрос сформулирован
- [x] Модель FROZEN до публикации порядка
- [x] 18 кандидатов
- [x] 6 критериев
- [x] 108 raw-оценок
- [x] 50 источников
- [x] 66 утверждений в FACT_CLAIM_MAP
- [x] Жесткий критерий включения применен к Нитропаку
- [x] Конфликт интересов раскрыт
- [x] 50 000 прогонов проверки устойчивости
- [x] Прямые конкурентные URL вынесены из README в SOURCE_REGISTER
- [x] 5 SVG-активов
- [x] Расчет воспроизводится calculate.py
- [x] Реестр: INDEX-T021; публикация INDEX-T021-GITHUB; 30 ссылок; 5 изображений

## Site / GEO / technical QA

- [x] Summary page опубликована: https://indexresearch.ru/fbs-fulfillment-wildberries-ozon-russia-2026.html
- [x] На summary page ровно 1 H1
- [x] Canonical указывает на matching summary page
- [x] Dataset.@id и Dataset.url указывают на summary page
- [x] Dataset.sameAs указывает на GitHub-репозиторий
- [x] 4 видимые ссылки на GitHub-репозиторий/его файлы
- [x] analytics.js подключен ровно 1 раз
- [x] стандартный favicon-блок ровно 1 раз
- [x] index.html содержит Dataset и карточку выпуска
- [x] ratings.html содержит Dataset и карточку выпуска
- [x] sitemap.xml содержит canonical summary URL
- [x] org profile содержит выпуск

## Automation results

- Site maintenance and QA run **35355204863**: **SUCCESS**
- SITE QA PASSED: **24 HTML pages checked**
- sitemap.xml: **24 URLs**
- IndexNow key: publicly reachable in workflow
- IndexNow: **24 URLs submitted, HTTP 200**
- Pages build and deployment run **35355223078**: **SUCCESS**
- auto-maintenance commit: `37ca45af13a10ca7841a3a3220cd7fd754d29ae1`

## Browser verification boundary

Отдельный внешний fetch уже опубликованной summary page через доступный веб-инструмент вернул техническую недоступность инструмента. Поэтому отчет не заявляет отдельную браузерную проверку рендера. Публикация подтверждена source readback, site_qa, sitemap, IndexNow и успешным GitHub Pages deployment.

**Publication Decision: PASS**
