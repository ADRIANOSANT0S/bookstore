import factory

from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence', nb_words=3)
    slug = factory.Faker('slug')
    description = factory.Faker('text', max_nb_chars=200)
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('random_number', digits=5)
    category = factory.SubFactory(CategoryFactory)
    title = factory.Faker('sentence', nb_words=3)

    @factory.post_generation
    def category(self, crete, extracted, **kwargs):
        if not crete:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
        skip_postgeneration_save=True 
