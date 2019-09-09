<template>
  <v-container>
    <v-layout
      row
      wrap
      v-if="planet"
    >
      <v-flex xs4>
        <v-container>
          <div
            v-html="planet.html"
          ></div>
        </v-container>
      </v-flex>
      <v-flex xs4>
        <v-container>
          <v-card>
            <v-card-title>
              <h3>Природа и люди</h3>
            </v-card-title>
            <v-container>
              <ul>
                <li>
                  <h4>{{planet.name}} как планета и ее изображение на карте</h4>
                  <ul>
                    <li
                      v-for="article in planet.about"
                      :key="article.title"
                    >
                      <article-contents
                        :title="article.title"
                        :url="article.url"
                        :children="article.children"
                      />
                    </li>
                    <li
                      v-if="planet.map"
                    >
                      <article-contents
                        :title="planet.map.title"
                        :url="`${planet.url}/map`"
                        :children="planet.map.wiki"
                      />
                    </li>
                  </ul>
                </li>
                <li>
                  <h4>Строение Земли</h4>
                  <ul>
                    <li v-if="planet.surface">
                      <article-contents
                        title="Поверхность Земли"
                        :url="planet.url"
                        :children="surface"
                      />
                    </li>
                    <li v-if="planet.magnet">
                      <article-contents
                        :title="planet.magnet.title"
                        :url="planet.url"
                        :children="list2pages(planet.magnet.pages)"
                      />
                    </li>
                  </ul>
                </li>
                <li v-if="land">
                  <h4>{{land.title || 'Суша'}}</h4>
                  <ul v-if="land.landscape">
                    <li>
                      <article-contents
                        :title="land.landscape.title"
                        :url="planet.url"
                        :children="list2pages(land.landscape.pages)"
                      />
                    </li>
                  </ul>
                </li>
                <li v-if="planet.surface.hydrosphere">
                  <h4>{{planet.surface.hydrosphere.title || 'Мировой океан'}}</h4>
                  <ul>
                    <li v-if="planet.surface.hydrosphere.seas">
                      <article-contents
                        :title="planet.surface.hydrosphere.seas.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.seas.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.currents">
                      <article-contents
                        :title="planet.surface.hydrosphere.currents.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.currents.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.flows">
                      <article-contents
                        :title="planet.surface.hydrosphere.flows.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.flows.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.tides">
                      <article-contents
                        :title="planet.surface.hydrosphere.tides.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.tides.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.glaciers">
                      <article-contents
                        :title="planet.surface.hydrosphere.glaciers.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.glaciers.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.avalanches">
                      <article-contents
                        :title="planet.surface.hydrosphere.avalanches.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.avalanches.pages)"
                      />
                    </li>
                    <li v-if="planet.surface.hydrosphere.landWaters">
                      <article-contents
                        :title="planet.surface.hydrosphere.landWaters.title"
                        :url="planet.url"
                        :children="list2pages(planet.surface.hydrosphere.landWaters.pages)"
                      />
                    </li>
                  </ul>
                </li>
                <li v-if="planet.surface.atmosphere">
                  <h4>{{planet.surface.atmosphere.title || 'Воздушный океан'}}</h4>
                  <ul>
                    <li>
                  * Атмосфера
                      * Тяжесть воздушного океана. Изобары
                      * Как образуется ветер. Циклоны и антициклоны
                      * Общая циркуляция атмосферы. Пассаты и антипассаты
                      * Водяной пар в воздухе
                      * Как образуется дождь и снег
                      * Воздушные массы приносят потепления и похолодания
                      * Признаки ухудшения погоды
                      * Как возникает ненастная погода. Фронт в атмосфере
                      * Теплый фронт
                      * Холодный фронт
                      * Предсказание погоды
                    </li>
                    <li>
                  * Грозные и "необыкновенные" явления в атмосфере
                      * Грозы
                          * 128/129
                      * Ливни и наводнения
                      * Градобития
                      * Шториы (бури), ураганы, тайфуны
                      * Шквалы
                      * Смерчи (торнадо, тромб)
                      * Местные бури
                      * Мираж
                      * Гало
                      * Радуга
                          * 144/145
                    </li>
                    <li>
                  * Как изучают погоду
                      * Метеорологические станции
                      * Синоптическая карта
                      * Метеорологическая и гидрологическая служба
                      * Оборудование метеорологической станции. Наблюдения за погодой
                      * Школьные метеорологические станции
                    </li>
                    <li>
                      Служба погоды в народном хозяйстве
                    </li>
                    <li>
                  * Климаты земного шара
                      * Погода и климат
                      * От чего зависит климат
                      * Самые холодные места на Земле
                      * Самые жаркие места на Земле
                      * Классификация климата
                      * Изменения климата
                          * 160/161
                      * Климатология
                      * Климат и человек
                    </li>
                  </ul>
                </li>

                <template v-if="planet.surface.biosphere">
                <li>
                  <h4>Почвы и растительность Земли</h4>
                  <ul>
                    <li>
                  * Почвы
                      * Структура почвы и ее значение
                      * Эрозия почв и борьба с ней
                      * Почвы тундры
                      * Почвы хвойно-лесной зоны
                      * Серые  и бурые почвы лиственных лесов
                      * Черноземные почвы степи
                          * 168/169
                      * Каштановые почвы сухой степи
                      * Почвы пустынь
                      * Почвы влажных субтропиков и тропической зоны
                      * Горные почвы
                      * Почвы речных пойм
                    </li>
                    <li>
                  * Растительный мир
                      * Растения дикорастущие и культурные. Ареал. Растительное сообщество
                      * Растительность и флора
                    </li>
                    <li>
                      Зона тундр
                    </li>
                    <li>
                      Зона лесов
                          * 176/177
                    </li>
                    <li>
                      Зона степей
                    </li>
                    <li>
                      Зона пустынь
                    </li>
                    <li>
                      Леса субтропиков
                          * 184/185
                    </li>
                    <li>
                      Зона тропической растительности
                    </li>
                  </ul>
                </li>
                <li>
                  <h4>Животный мир земного шара</h4>
                  <ul>
                    <li>
                  * Животный мир суши
                      * Животные Арктики и Антарктики
                          * 192/193
                      * Животные тундры
                      * Животные тайги
                      * Обитатели пояса широколиственных лесов
                      * Животные степей и саванн
                          * 200/201
                      * Животные пустынь
                      * Животные тропического леса
                          * 208/209
                      * Австралийская область
                      * Неотропическая область
                      * Эфиопская область
                      * Индо-Малайская область
                      * Голарктическая область
                    </li>
                    <li>
                  * Жизнь в океанах и морях
                      * Водная среда и ее особенности
                      * От поверхности моря до океанских глубин
                      * По морям и океанам
                          * 224/225
                    </li>
                    <li>
                  * Открыватели морских тайн
                      * Организация исследований
                      * Работа на станции
                      * Исследования дна моря и его обитателей
                      * Исследование геологического строения дна моря
                      * Изучение погоды
                    </li>
                  </ul>
                </li>
                </template>

                <li>
                  <h4>Население Земли</h4>
                  <ul>
                    <li>
                  * Население земного шара
                      * Может ли быть Земля перенаселена
                      * Расселение людей на Земле. Плотность населения
                      * Расы людей
                      * Основные расы и их современное распространение
                      * Происхождение рас
                      * Языки народов мира
                      * Языковое родство народов
                      * Племена, народности и нации
                          * 240/241
                    </li>
                  </ul>
                </li>
                <li>
                  <h4>СССР на карте мира</h4>
                  <ul>
                    <li>
                  * СССР - страна строящегося коммунизма
                      * Арктика (ледяная зона)
                      * Зона тундры
                      * Зона лесов
                      * Зона степей
                      * Зона полупустынь и пустынь
                      * Горы
                          * 264/265
                          * 264/265
                      * Субтропики
                      * Страна сокровищ
                      * Государство нового типа
                      * Москва
                    </li>
                  </ul>
                </li>
              </ul>
            </v-container>
          </v-card>
        </v-container>
      </v-flex>
      <v-flex xs4>
            <v-container>
              <v-card>
                <v-card-title>
                  <h3>Исследователи Земли</h3>
                </v-card-title>
                <v-container>
                <h4>Старинные землепроходцы и мореплаватели</h4>
                <ul>
                  <li>
                    Китайский землепроходец Чжан Цянь
                  </li>
                  <li>
                    По следам малайских мореходов
                  </li>
                  <li>
                    Марко Поло
                  </li>
                  <li>
                    Путешествия в Индию Афанасия Никитина
                  </li>
                </ul>
                <h4>Эпоха великих географических открытий</h4>
                <ul>
                  <li>
                    Великие географические открытия
                  </li>
                  <li>
                    Подвиг Колумба
                  </li>
                  <li>
                    Морской путь в Индию
                  </li>
                  <li>
                    "Южное море" - Тихий океан
                  </li>
                  <li>
                    Откуда произошло название "Америка"
                  </li>
                  <li>
                    Первое кругосветное плавание
                  </li>
                  <li>
                    Открытие Австралии
                  </li>
                  <li>
                    Землепроходцы на Тихом океане
                  </li>
                  <li>
                    Поход Василия Пояркова на Амур
                  </li>
                  <li>
                    Русский землепроходец Ерофей Павлович Хабаров
                  </li>
                  <li>
                    Открытие пролива между Азией и Америкой
                  </li>
                </ul>
                <h4>Географические открытия и исследования XVIII в.</h4>
                <ul>
                  <li>
                * Экспедиции В. Беринга и А. И. Чирикова
                    * Первая Камчатская экспедиция
                    * Вторая Камчатская экспедиция
                    * Плавание В. Беринга к Америке
                    * Плавание А. И. Чирикова
                    * Плавание к берегам Японии
                  </li>
                  <li>
                * Великая Северная экспедиция
                    * Плавания от Архангельска до устья Оби
                    * От Оби до Енисея
                    * От устья Лены к Енисею
                    * На восток от Лены
                  </li>
                  <li>
                    Михаил Васильевич Ломоносов как географ
                  </li>
                  <li>
                    Русский мореплаватель и исследователь Америки Г. И. Шелихов
                  </li>
                  <li>
                    Плавания Джеймса Кука
                  </li>
                </ul>
                <h4>Исследования XIX и XX вв.</h4>
                <ul>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                    </li>
                  </ul>
                  <h4>Завоевание высоких широт</h4>
                  <ul>
                    <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                    * Марко Поло
                    * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                    </li>
                  </ul>
                  <h4>Юные географы, краеведы, путешественники</h4>
                  <ul>
                    <li>
                * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                    * Марко Поло
                        * 504/505
                    * Марко Поло
                    * Марко Поло
                    * Марко Поло
                    * Марко Поло
                  </li>
                  <li>
                * Марко Поло
                        * 512/513
                    </li>
                  </ul>
                </v-container>
              </v-card>
            </v-container>
      </v-flex>
      <v-flex xs4>
            <v-container>
              <v-card>
                <v-card-title>
                  <h3>Справочный отдел</h3>
                </v-card-title>
                <v-container>
                  <ul>
                    <li>
                      Справочные сведения о Земле
                    </li>
                    <li>
                      Хронологические таблицы
                        * Древний мир
                        * Средние века
                        * Новое время
                    </li>
                    <li>
                      Что читать по географии
                        * Общее землеведение
                        * Воздушная оболочка Земли
                        * Водная оболочка Земли
                        * Суша
                        * География СССР
                        * История географических исследований и развития географических знаний
                        * Советские исследования в Арктике и Антарктике
                        * Выдающиеся русские географы и путешественники
                        * Выдающиеся зарубежные географы и путешественники
                        * В помощь юным географам и краеведам
                    </li>
                    <li>
                      Указатель имен и предметов
                    </li>
                  </ul>
                </v-container>
              </v-card>
            </v-container>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Planet',
  components: {
    ArticleContents: () => import('@/components/ArticleContents.vue'),
  },
  props: [
    'planet',
  ],
  computed: {
    land() { return this.planet && this.planet.surface && this.planet.surface.land; },
    surface() {
      const surface = [];
      if (!this.planet || !this.planet.surface) {
        return surface;
      }
      if (this.planet.surface.hydrosphere) {
        surface.push({ url: this.planet.url, title: 'Мировой океан' });
      }
      if (this.planet.surface.atmosphere) {
        surface.push({ url: this.planet.url, title: 'Воздушный океан' });
      }
      if (this.planet.surface.biosphere) {
        surface.push({ url: this.planet.url, title: 'Сфера жизни' });
      }
      if (this.planet.surface.density) {
        surface.push({ url: this.planet.url, title: 'Плотность Земли' });
      }
      return surface;
    },
  },
  methods: {
    list2pages: pages => (pages || []).map(page => ({
      title: page,
      url: '/',
    })),
  },
};
</script>

<style scoped>

</style>
