from config import db
from models.category import Category
from schemas.category import CreateCategorySchema

class CategoryService():
  def get_all_categories(self):
    pass

  def get_category(self, id):
    return db.get_or_404(Category, id)

  def create_category(self, category_info):
    category = None

    if category_info['parent'] is not None:
      parent_category = db.get_or_404(Category, category_info['parent'])

      category = Category(
        name=category_info['name'], parent_id=parent_category.id
      )
    else:
      category = Category(
        name=category_info['name']
      )

    db.session.add(category)
    db.session.commit()
    db.session.refresh(category)

    return category

  def delete_category(self, id):
    pass