import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Properties;

public class ConnectToPostgreSQL {

    public static void main(String[] args)
        throws Exception
    {
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "");

        String uri = "jdbc:postgresql://localhost:5432/postgres";

        System.out.printf("Attempting to connect to: %s...\n", uri);
        Connection connect = DriverManager.getConnection(uri, props);
        System.out.println("> Connected successfully!!");
        connect.close();
    }
}
