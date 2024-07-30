package javamongodb;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.Document;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

import static com.mongodb.client.model.Accumulators.sum;
import static com.mongodb.client.model.Aggregates.group;
import static com.mongodb.client.model.Aggregates.match;
import static com.mongodb.client.model.Aggregates.project;
import static com.mongodb.client.model.Filters.and;
import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Filters.exists;
import static com.mongodb.client.model.Filters.gt;
import static com.mongodb.client.model.Filters.gte;
import static com.mongodb.client.model.Filters.lt;
import static com.mongodb.client.model.Filters.lte;
import static com.mongodb.client.model.Projections.excludeId;
import static com.mongodb.client.model.Sorts.descending;
import static com.mongodb.client.model.Updates.inc;
import static com.mongodb.client.model.Updates.set;

import static java.util.Arrays.asList;
import static java.util.Collections.singletonList;
/**
 * The using Java with MongoDB code example
 */
public class JavaMongoDB {
    /**
     * Run this main method to see the output of this quick example.
     *
     * @param args takes an optional single argument for the connection string
     */
    public static void main(final String[] args) {
        // Creating a Mongo client
        Mongo client = new Mongo("localhose", 27017);

        // Accessing the database
        DB database = mongo.getDB("Unit5");

        //List All Databases
        List<String> dbs = mongo.getDatabaseNames();
        for(String db : dbs){
            System.out.println(db);
        }

        // drop all the data in it
        // collection.drop();

        // add code to make a document and insert it into the collection. Print results to console
        // System.out.println(myDoc.toJson());

        // Clean up
//        database.drop();

        // release resources
//        mongoClient.close();
    }
}
