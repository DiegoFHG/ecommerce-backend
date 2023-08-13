from sqlalchemy import text
from config import db
from models.category import Category

class CategoryService():
  def get_all_categories(self, parents_only):
    categories = None

    if parents_only:
      categories = Category.query.filter_by(parent_id=None).all()
    else:
      categories = Category.query.all()

    return categories

  def get_category(self, id):
    return db.get_or_404(Category, id)

  def get_category_subcategories(self, id):
    category = db.get_or_404(Category, id)
    subcategories = Category.query.filter_by(parent_id=category.id)

    return subcategories   

  def get_category_tree(self, id):
    category = db.get_or_404(Category, id)
    tree = db.session.execute(
      text("""WITH RECURSIVE tree AS (
        SELECT 
          id, name, parent_id, created_at, updated_at, deleted_at
        FROM categories
        WHERE id = :id
        UNION
          SELECT 
            c.id, c.name, c.parent_id, c.created_at, c.updated_at, c.deleted_at
          FROM categories c
          INNER JOIN tree t ON t.parent_id = c.id
      ) SELECT * FROM tree ORDER by tree.id ASC"""),
      { 'id': category.id }
    ).all()

    return tree

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