from base import Base
import pymongo
import os


# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from the Base class to a MongoDB instance.
    Initializes an instance of the inherited class.
    
    Defined methods are as follows:.
    upload_collection: upload an entire document of items to MongoDB
    delete_collection: drops an entire collection of data
    '''
    
    def __init__(self):
        # Load the env variables:
        self.__mongo_url = os.getenv('MONGO_URL')
        #Connect to PyMongo
        self.client = pymongo.MongoClient("mongodb+srv://basic:basic1234@news-api.uggm4x0.mongodb.net/?retryWrites=true&w=majority")
        # Create a database
        self.db = self.client.db
        # Create a collection:
        self.news_info = self.db.news_info
        
        
    def upload_collection(self):
        self.news_info.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        self.news_info.drop()
        
        Base.__init__(self)
        # self.df.set_index('id', inplace=True)
        for i in self.df.index:
            self.news_info.insert_one(self.df.loc[i].to_dict())
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Park Info to Mongo')