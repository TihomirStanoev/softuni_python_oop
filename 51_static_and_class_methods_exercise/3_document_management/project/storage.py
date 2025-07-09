from project.topic import Topic
from project.category import Category
from project.document import Document

class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def _get_item_by_id(self, items, item_id):
        return next((item for item in items if item.id == item_id), None)

    def edit_category(self, category_id, new_name):
        category = self._get_item_by_id(self.categories, category_id)

        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self._get_item_by_id(self.topics, topic_id)

        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self._get_item_by_id(self.documents, document_id)

        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self._get_item_by_id(self.categories, category_id)

        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self._get_item_by_id(self.topics, topic_id)

        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self._get_item_by_id(self.documents, document_id)

        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self._get_item_by_id(self.documents, document_id)

        if document:
            return document

    def __repr__(self):
        result = [str(document) for document in self.documents]
        return '\n'.join(result)