<template>
  <v-container>
    <portal v-model="enteringPortal" />

    <v-card
      v-if="world"
    >
      <v-img
        v-if="world.image"
        :src="world.image"
        height="200px"
      />

      <v-container>
        <v-layout row wrap>
          <v-flex xs3>
            <v-card>
              <v-card-actions>
                <v-btn
                  to="/"
                  icon
                >
                  <v-icon>view_module</v-icon>
                </v-btn>
                <v-btn
                  to="/random-world"
                  icon
                >
                  <v-icon>gesture</v-icon>
                </v-btn>
              </v-card-actions>

              <v-card-actions
                v-if="world.wiki"
              >
                <v-btn
                  v-for="(href, k) in world.wiki"
                  :key="k"
                  :href="href"
                  target="_blank"
                  icon
                >
                  <v-avatar
                    :size="32"
                  >
                    <img
                      v-if="wikiLogo[k]"
                      :src="wikiLogo[k]"
                      :alt="k"
                    >
                    <span
                      v-else
                    >
                      {{k}}
                    </span>
                  </v-avatar>
                </v-btn>
              </v-card-actions>

              <v-list>
                <v-list-tile
                  :to="world.url"
                >
                  <v-list-tile-content>
                    <v-list-tile-title>
                      Главная
                    </v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile
                  v-for="(page, id) in world.pages"
                  :key="`page-${id}`"
                  :to="`/wiki/${page.url}`"
                >
                  <v-list-tile-content>
                    <v-list-tile-title v-text="page.filename" />
                  </v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
            <br />

            <template
              v-for="(v, id) in encyclo.child"
            >
              <v-card
                :key="`v${id}`"
              >
                <v-card-title>
                  Детская энциклопедия (Издание {{id + 1}})
                </v-card-title>
                <v-list>
                  <v-list-tile
                    v-for="volume in v"
                    :key="`v1-${volume.id}`"
                    :to="`/world/${world.slug}/${volume.to}`"
                  >
                    <v-list-tile-content>
                      <v-list-tile-title v-text="volume.title" />
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
              </v-card>
              <br />
            </template>
          </v-flex>
          <v-flex xs9>
            <v-card-title
              class="headline"
              :to="world.to"
              v-text="world.title"
            />

            <slot />

            <!-- Object.keys(world) -->
            <!-- world.title -->
            <!-- world.image -->
            <!-- world.url -->
            <!-- world.text -->
            <!-- world.html -->

            <v-card-text
              v-if="wiki"
              v-html="wiki"
            />
            <v-card-text
              v-else
              v-html="world.html"
            />
          </v-flex>
        </v-layout>

      </v-container>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>favorite</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>bookmark</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>share</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import wikipedia from '@/assets/wiki/wiki.png';
import lurkmore from '@/assets/wiki/lurk.png';
import posmotreli from '@/assets/wiki/posmotreli.png';

export default {
  name: 'World',
  components: {
    Portal: () => import('@/components/Portal.vue'),
  },
  props: [
    'world',
    'wiki',
  ],
  data: () => ({
    enteringPortal: true,
    wikiLogo: {
      wikipedia,
      lurkmore,
      posmotreli,
    },
    encyclo: {
      child: [
        [
          {id: 1, title: 'Земля', to: 'earth'},
          {id: 2, title: 'Земная кора и недра Земли. Мир небесных тел', to: 'earth/geology/+/astronomy'},
          {id: 3, title: 'Числа и фигуры. Вещество и энергия', to: 'math/+/energy'},
          {id: 4, title: 'Растения и животные', to: 'biology'},
          {id: 5, title: 'Техника', to: 'tech'},
          {id: 6, title: 'Человек', to: 'human'},
          {id: 7, title: 'Из истории человеческого общества', to: 'history'},
          {id: 8, title: 'Литература и искусство', to: 'art'},
          {id: 9, title: 'Наша советская Родина', to: 'motherland'},
          {id: 10, title: 'Зарубежные страны', to: 'countries'},
        ],
        [
          {id: 1, title: 'Земля', to: 'earth'},
          {id: 2, title: 'Мир небесных тел. Числа и фигуры', to: 'astronomy/+/math'},
          {id: 3, title: 'Растения и животные', to: 'biology'},
          {id: 4, title: 'Техника и производство', to: 'tech'},
          {id: 5, title: 'Вещество и энергия', to: 'energy'},
          {id: 6, title: 'Человек', to: 'human'},
          {id: 7, title: 'Сельское хозяйство', to: 'agriculture'},
          {id: 8, title: 'Из истории человеческого общества', to: 'history'},
          {id: 9, title: 'Зарубежные страны', to: 'countries'},
          {id: 10, title: 'Язык. Художественная литература', to: 'language'},
          {id: 11, title: 'Искусство', to: 'art'},
          {id: 12, title: 'Наша советская Родина', to: 'motherland'},
        ],
        [
          {id: 1, title: 'Земля', to: 'earth'},
          {id: 2, title: 'Мир небесных тел. Числа и фигуры', to: 'astronomy/+/math'},
          {id: 3, title: 'Вещество и энергия', to: 'energy'},
          {id: 4, title: 'Растения и животные', to: 'biology'},
          {id: 5, title: 'Техника и производство', to: 'tech'},
          {id: 6, title: 'Сельское хозяйство', to: 'agriculture'},
          {id: 7, title: 'Человек', to: 'human'},
          {id: 8, title: 'Из истории человеческого общества', to: 'history'},
          {id: 9, title: 'Язык и литература', to: 'language'},
          {id: 10, title: 'Зарубежные страны', to: 'countries'},
          {id: 11, title: 'Искусство', to: 'art'},
          {id: 12, title: 'Наша советская Родина', to: 'motherland'},
        ],
      ],
    },
    forChild: {
      /*
      Всемирная история
      Биология
      География
      Геология
      История России
      Религии мира
      Искусство
      Астрономия
      Русская литература
      Языкознание. Русский язык

      Математика
      Россия: физическая и экономическая география
      Страны. Народы. Цивилизации
      Техника
      Всемирная литература
      Физика
      Химия
      Человек
      Экология
      Спорт

      Общество
      Информатика
      Универсальный иллюстрированный энциклопедический словарь
      Домашние питомцы
      Космонавтика
      Бизнес
      Великие люди мира
      Толковый словарь русского языка
      Москвоведение
      Санкт-Петербург (планируется)

      Древние цивилизации
      История войн
      Толковый словарь школьника
      История Древнего мира
      История Средних веков
      История Нового Времени. XV — начало XIX века
      История XIX—XX вв. Новое и Новейшее время
      Языки мира
      Компьютер
      Россия: Православие

      Иллюстрированный атлас мира
      Великая Отечественная война
      Ботаника
      Мифология
      Политика (заявлен как 27 том)

      Дополнительные тома

      Птицы и звери
      Человечество. XXI век (ранее был 30-м томом)
      Выбор профессии (ранее был 34-м томом)

      Более не выпускаемые тома

      Всемирная история (ранняя версия, охватывающая всю мировую историю в одной книге)
      Российские столицы. Москва и Санкт-Петербург
      Языкознание. Русский язык (ранее был 10-м томом)
      Личная безопасность
      История XX века. Зарубежные страны

      Планировавшиеся к выпуску тома

      Санкт-Петербург
      Философия
      Электроника и электротехника
       */
    },
    whatIsWhat: {
      /*
      Семь чудес света
      Путешественники-первооткрыватели
      Стихийные бедствия
      Древние греки
      Динозавры
      Время
      Погода
      Атомная энергия
      Гладиаторы
      Слоны

      Звёзды
      Крестоносцы
      Ведьмы
      Солнце
      Пирамиды
      Лошади
      Мосты
      Кошки
      Сокровища
      Собаки

      Пираты
      Пещеры
      Самураи
      Человекообразные обезьяны
      Флаги
      Деревья
      Мультимедиа
      Птицы
      Загадочные явления
      Арктика и Антарктика

      Наше тело
      Рыбы
      Тропический лес
      Internet (специальный выпуск)
       */
    },
    collections: {
      /*
          100 битв, которые изменили мир
          Slippets
      !   Автолегенды СССР
      -   Автомобиль на службе
      !   Атлас. Целый мир в твоих руках
      -   Балет. Лучшее на DVD
      !   Винни и его друзья. Веселые истории
          Восхождение
      -   Галилео. Наука опытным путём
      !   Дамы эпохи. Моя коллекция кукол

      !   Двенадцать апостолов
          Динозавры и мир юрского периода
          Дворцы и усадьбы
      -   Дом мечты
      !   Животные леса
      -   Животные на ферме
          Занимательные головоломки
      !   Знаменитые династии России
      !   Искусство рисования и живописи
      !   История в женских портретах

      -   Коллекция Золотой глобус. Захватывающее путешествие на DVD
      !   Комнатные и садовые растения
      !   Корабль адмирала Нельсона «Виктори»
      !   Куклы в костюмах народов мира
      ?   Куклы в маскарадных костюмах
      !   Куклы в народных костюмах
      !-  Легендарные самолёты
      -   М20 «Победа»
      !?  М21 "Волга"
      -   ЗИС-110

          Маджики. Котята
      !   Минералы. Сокровища Земли
      -   Мир математики
      -   Мировая авиация
      !   Монеты и банкноты
      -   Наследие человечества
      !?- Насекомые и их знакомые
      !   Наука. Величайшие теории
      -?  Наша история 100 Великих имен
      !   Парфюм. Коллекция миниатюр

          Повелитель морей
      !   Полицейские машины мира
      !   Православные храмы. Путешествие по святым местам
          Путешествие по Европе
      -   Робот шпион (журнал)
          Скуби-Ду. Великие тайны мира
      ?   Собери и изучи тело человека
          Соберите своего R2-D2
      -   Собери свой телескоп
      !   Супергерои Marvel. Шахматный курс

      -   Суперкары. Лучшие автомобили мира
      !   Художественная галерея
      -   Шахматы Гарри Поттер
      !   Шедевры мировой литературы в миниатюре
      !-  Энергия камней
          Языковые курсы «English от Де Агостини»
       */
    },
  }),
};
</script>

<style scoped>

</style>
