<template>
  <v-tabs>
    <v-tab>
      Версия 1
    </v-tab>
    <v-tab>
      Версия 2
    </v-tab>
    <v-tab>
      Версия 3
    </v-tab>
    <v-tab
      v-for="(v, id) in encyclo.child"
      :key="`tab-${id}`"
    >
      Издание {{id + 1}}
    </v-tab>

    <v-tab-item>
      <v-card flat>
        <v-card-title>
          Версия 1
        </v-card-title>
        <v-layout
          row
          wrap
        >
          <v-flex xs6>
            <v-container>
              <planet />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <geology />
            </v-container>
            <v-container>
              <astronomy />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <maths />
            </v-container>
            <v-container>
              <physics />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <agriculture />
            </v-container>
            <v-container>
              <biology />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <tech />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <v-card>
                <v-card-title>
                  Расы
                </v-card-title>
                <v-container>
                  <race />
                </v-container>
              </v-card>
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <history />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <literature />
            </v-container>
            <v-container>
              <art />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <country />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <countries />
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-tab-item>
    <v-tab-item>
      <v-card flat>
        <v-card-title>
          Версия 2
        </v-card-title>
        <v-layout
          row
          wrap
        >
          <v-flex xs6>
            <v-container>
              <planet />
            </v-container>
            <v-container>
              <geology />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <astronomy />
            </v-container>
            <v-container>
              <maths />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <biology />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <tech />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <physics />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <v-card>
                <v-card-title>
                  Расы
                </v-card-title>
                <v-container>
                  <race />
                </v-container>
              </v-card>
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <agriculture />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <history />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <countries />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <literature />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <art />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <country />
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-tab-item>
    <v-tab-item>
      <v-card flat>
        <v-card-title>
          Версия 3
        </v-card-title>
        <v-layout
          row
          wrap
        >
          <v-flex xs6>
            <v-container>
              <planet />
            </v-container>
            <v-container>
              <geology />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <astronomy />
            </v-container>
            <v-container>
              <maths />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <physics />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <biology />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <tech />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <agriculture />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <v-card>
                <v-card-title>
                  Расы
                </v-card-title>
                <v-container>
                  <race />
                </v-container>
              </v-card>
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <history />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <literature />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <countries />
            </v-container>
          </v-flex>

          <v-flex xs6>
            <v-container>
              <art />
            </v-container>
          </v-flex>
          <v-flex xs6>
            <v-container>
              <country />
            </v-container>
          </v-flex>
        </v-layout>
      </v-card>
    </v-tab-item>

    <v-tab-item
      v-for="(v, id) in encyclo.child"
      :key="`page-${id}`"
    >
      <v-card
        flat
      >
        <v-card-title>
          Детская энциклопедия
        </v-card-title>
        <v-list>
          <v-list-item
            v-for="volume in v"
            :key="`volume-${volume.id}`"
            :to="volume.to"
          >
            <v-list-item-content>
              <v-list-item-title v-text="volume.title" />
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
export default {
  name: 'WorldVolumes',
  components: {
    Planet: () => import('@/components/volumes/Planet.vue'),
    Geology: () => import('@/components/volumes/Geology.vue'),
    Astronomy: () => import('@/components/volumes/Astronomy.vue'),
    Maths: () => import('@/components/volumes/Maths.vue'),
    Physics: () => import('@/components/volumes/Physics.vue'),
    Biology: () => import('@/components/volumes/Biology.vue'),
    Tech: () => import('@/components/volumes/Tech.vue'),
    Race: () => import('@/components/volumes/Race.vue'),
    History: () => import('@/components/volumes/History.vue'),
    Art: () => import('@/components/volumes/Art.vue'),
    Country: () => import('@/components/volumes/Country.vue'),
    Countries: () => import('@/components/volumes/Countries.vue'),
    Agriculture: () => import('@/components/volumes/Agriculture.vue'),
    Literature: () => import('@/components/volumes/Literature.vue'),
  },
  data: () => ({
    encyclo: {
      child: [
        [
          { id: 1, title: 'Земля', to: 'planet-earth' },
          { id: 2, title: 'Земная кора и недра Земли. Мир небесных тел', to: 'planet-earth/geology/+/astronomy' },
          { id: 3, title: 'Числа и фигуры. Вещество и энергия', to: 'math/+/energy' },
          { id: 4, title: 'Растения и животные', to: 'biology' },
          { id: 5, title: 'Техника', to: 'tech' },
          { id: 6, title: 'Человек', to: 'human' },
          { id: 7, title: 'Из истории человеческого общества', to: 'history' },
          { id: 8, title: 'Литература и искусство', to: 'art' },
          { id: 9, title: 'Наша советская Родина', to: 'motherland' },
          { id: 10, title: 'Зарубежные страны', to: 'countries' },
        ],
        [
          { id: 1, title: 'Земля', to: 'planet-earth' },
          { id: 2, title: 'Мир небесных тел. Числа и фигуры', to: 'astronomy/+/math' },
          { id: 3, title: 'Растения и животные', to: 'biology' },
          { id: 4, title: 'Техника и производство', to: 'tech' },
          { id: 5, title: 'Вещество и энергия', to: 'energy' },
          { id: 6, title: 'Человек', to: 'human' },
          { id: 7, title: 'Сельское хозяйство', to: 'agriculture' },
          { id: 8, title: 'Из истории человеческого общества', to: 'history' },
          { id: 9, title: 'Зарубежные страны', to: 'countries' },
          { id: 10, title: 'Язык. Художественная литература', to: 'language' },
          { id: 11, title: 'Искусство', to: 'art' },
          { id: 12, title: 'Наша советская Родина', to: 'motherland' },
        ],
        [
          { id: 1, title: 'Земля', to: 'planet-earth' },
          { id: 2, title: 'Мир небесных тел. Числа и фигуры', to: 'astronomy/+/math' },
          { id: 3, title: 'Вещество и энергия', to: 'energy' },
          { id: 4, title: 'Растения и животные', to: 'biology' },
          { id: 5, title: 'Техника и производство', to: 'tech' },
          { id: 6, title: 'Сельское хозяйство', to: 'agriculture' },
          { id: 7, title: 'Человек', to: 'human' },
          { id: 8, title: 'Из истории человеческого общества', to: 'history' },
          { id: 9, title: 'Язык и литература', to: 'language' },
          { id: 10, title: 'Зарубежные страны', to: 'countries' },
          { id: 11, title: 'Искусство', to: 'art' },
          { id: 12, title: 'Наша советская Родина', to: 'motherland' },
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
