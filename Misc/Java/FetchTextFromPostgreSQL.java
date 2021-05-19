import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.DriverManager;
import java.util.Properties;

public class FetchTextFromPostgreSQL {

    static final String QUERY =
        "SELECT raw_description, url_link FROM product_content WHERE cd_product = ?";

    public static void main(String[] args)
        throws Exception
    {
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "");

        String uri = "jdbc:postgresql://localhost:5432/sandbox";
        System.out.printf("Attempting to connect to: %s...\n", uri);
        try (Connection conn = DriverManager.getConnection(uri, props)) {
            System.out.printf("> Connected successfully!!\n");

            System.out.printf("Attempting to fetch data...\n");
            PreparedStatement stmt = conn.prepareStatement(QUERY);
            stmt.setString(1, "110001");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                System.out.printf("> %s, %s\n", rs.getString(1), rs.getString(2));
            }
            rs.close();
            System.out.printf("> All data fetch successfully!!\n");
        } catch (Exception ex) {
            System.out.printf("Oops: something is wrong... %s", ex);
        }
    }
}
