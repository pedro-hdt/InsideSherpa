import org.junit.Test;

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

import static org.junit.Assert.*;

public class DataCruncherTest {
    private final DataCruncher dataCruncher = new DataCruncher();

    // ignore
    @Test
    public void readAllTransactions() throws Exception {
        var transactions = dataCruncher.readAllTransactions();
        assertEquals(594643, transactions.size());
    }

    // example
    @Test
    public void readAllTransactionsAge0() throws Exception {
        var transactions = dataCruncher.readAllTransactionsAge0();
        assertEquals(3630, transactions.size());
    }

    // task1
    @Test
    public void getUniqueMerchantIds() throws Exception {
        var transactions = dataCruncher.getUniqueMerchantIds();
        assertEquals(50, transactions.size());
    }

    // task2
    @Test
    public void getTotalNumberOfFraudulentTransactions() throws Exception {
        var totalNumberOfFraudulentTransactions = dataCruncher.getTotalNumberOfFraudulentTransactions();
        assertEquals(297508, totalNumberOfFraudulentTransactions);
    }

    // task3
    @Test
    public void getTotalNumberOfTransactions() throws Exception {
        assertEquals(297508, dataCruncher.getTotalNumberOfTransactions(true));
        assertEquals(297135, dataCruncher.getTotalNumberOfTransactions(false));
    }

    // task4
    @Test
    public void getFraudulentTransactionsForMerchantId() throws Exception {
        Set<Transaction> fraudulentTransactionsForMerchantId =
                dataCruncher.getFraudulentTransactionsForMerchantId("M1823072687");
        assertEquals(149001, fraudulentTransactionsForMerchantId.size());
    }

    // task5
    @Test
    public void getTransactionForMerchantId() throws Exception {
        assertEquals(102588,
                dataCruncher.getTransactionsForMerchantId("M348934600", true).size());
        assertEquals(102140,
                dataCruncher.getTransactionsForMerchantId("M348934600", false).size());
    }

    // task6
    @Test
    public void getAllTransactionSortedByAmount() throws Exception {
        List<Transaction> allTransactionsSortedByAmount = dataCruncher.getAllTransactionsSortedByAmount();
        double previousAmount = -Double.MAX_VALUE;
        for (Transaction t : allTransactionsSortedByAmount) {
            // regular comparison operators should do fine if not for exact equality
            assertTrue(t.getAmount() >= previousAmount);
            previousAmount = t.getAmount();
        } // performance is not great but checking all elements is the only way to "prove" correctness
    }

    // task7
    @Test
    public void getFraudPercentageForMen() throws Exception {
        double fraudPercentageForMen = dataCruncher.getFraudPercentageForMen();
        assertEquals(0.45, fraudPercentageForMen, 0.01);
    }

    // task8
    @Test
    public void getCustomerIdsWithNumberOfFraudulentTransactions() throws Exception {
        // Warning: depends on DataCruncher#getCustomerIdToNumberOfTransactions() being correct

        // if we pass in 0 as the lower limit for including a customer, this should be the same as just getting the
        // keyset of the map returned from task 9
        Set<String> customerIdsWithNumberOfFraudulentTransactions =
                dataCruncher.getCustomerIdsWithNumberOfFraudulentTransactions(0); // should return all customer ids
        Set<String> expectedCustomerIdsWithNumberOfTransactions =
                dataCruncher.getCustomerIdToNumberOfTransactions().keySet();
        assertEquals(expectedCustomerIdsWithNumberOfTransactions, customerIdsWithNumberOfFraudulentTransactions);
    }

    // task9
    @Test
    public void getCustomerIdToNumberOfTransactions() throws Exception {
        // Warning: depends on DataCruncher#getTotalNumberOfFraudulentTransactions() being correct

        Map<String, Integer> customerIdToNumberOfTransactions = dataCruncher.getCustomerIdToNumberOfTransactions();

        // total number of fraudulent transactions should be the same regardless of how it is grouped
        long totalFraudulentTransactions = customerIdToNumberOfTransactions.values().stream()
                .mapToLong(Integer::intValue)
                .sum();
        long expectedFraudulentTransactions = dataCruncher.getTotalNumberOfFraudulentTransactions();
        assertEquals(expectedFraudulentTransactions, totalFraudulentTransactions);
    }

    // task10
    @Test
    public void getMerchantIdToTotalAmountOfFraudulentTransactions() throws Exception {
        Map<String, Double> merchantIdToTotalAmountOfFraudulentTransactions =
                dataCruncher.getMerchantIdToTotalAmountOfFraudulentTransactions();

        // sum of amounts of all fraudulent transactions should be the same regardless of how it is grouped
        double expectedFraudulentAmount = dataCruncher.readAllTransactions().stream()
                .filter(Transaction::isFraud)
                .map(Transaction::getAmount)
                .mapToDouble(Double::doubleValue)
                .sum();
        double fraudulentAmountWhenGroupedByMerchant = merchantIdToTotalAmountOfFraudulentTransactions.values().stream()
                .mapToDouble(Double::doubleValue)
                .sum();
        assertEquals(expectedFraudulentAmount, fraudulentAmountWhenGroupedByMerchant, 0.01);
    }
}