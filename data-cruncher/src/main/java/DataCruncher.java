import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class DataCruncher {

    // do not modify this method - just use it to get all the Transactions that are in scope for the exercise
    public List<Transaction> readAllTransactions() throws Exception {
        return Files.readAllLines(Paths.get("src/main/resources/payments.csv"), StandardCharsets.UTF_8)
                .stream()
                .skip(1)
                .map(line -> {
                    var commaSeparatedLine = List.of(line
                            .replaceAll("'", "")
                            .split(",")
                    );
                    var ageString = commaSeparatedLine.get(2);
                    var ageInt = "U".equals(ageString) ? 0 : Integer.parseInt(ageString);
                    return new Transaction(commaSeparatedLine.get(1),
                            ageInt,
                            commaSeparatedLine.get(3),
                            commaSeparatedLine.get(4),
                            commaSeparatedLine.get(5),
                            commaSeparatedLine.get(6),
                            commaSeparatedLine.get(7),
                            Double.parseDouble(commaSeparatedLine.get(8)),
                            "1".equals(commaSeparatedLine.get(9)));
                })
                .collect(Collectors.toList());
    }

    // example
    public List<Transaction> readAllTransactionsAge0() throws Exception {
        return readAllTransactions().stream()
                .filter(transaction -> transaction.getAge() == 0)
                .collect(Collectors.toList());
    }

    // task 1
    public Set<String> getUniqueMerchantIds() throws Exception {
        return readAllTransactions().stream()
                .map(Transaction::getMerchantId) // extract merchant Ids
                .collect(Collectors.toSet()); // collecting to set automatically makes these unique
    }

    // task 2
    public long getTotalNumberOfFraudulentTransactions() throws Exception {
        return getTotalNumberOfTransactions(true);
    }

    // task 3
    public long getTotalNumberOfTransactions(boolean isFraud) throws Exception {
        return readAllTransactions().stream()
                .filter(transaction -> isFraud == transaction.isFraud()) // extract only fraudulent/non-fraudulent
                .count();
    }

    // task 4
    public Set<Transaction> getFraudulentTransactionsForMerchantId(String merchantId) throws Exception {
        return getTransactionsForMerchantId(merchantId, true);
    }

    // task 5
    public Set<Transaction> getTransactionsForMerchantId(String merchantId, boolean isFraud) throws Exception {
        return readAllTransactions().stream()
                .filter(transaction -> (merchantId.equals(transaction.getMerchantId()))) // extract for this merchant
                .filter(transaction -> isFraud == transaction.isFraud()) // pick up only the fraudulent (or not)
                .collect(Collectors.toSet());
    }

    // task 6
    public List<Transaction> getAllTransactionsSortedByAmount() throws Exception {
        return readAllTransactions().stream()
                .sorted(Comparator.comparingDouble(Transaction::getAmount)) // in ascending order
                .collect(Collectors.toList());
    }

    // task 7
    public double getFraudPercentageForMen() throws Exception {
        // For clarification, this method answers the following question:
        // Out of the fraudulent transactions, how many were men?
        // And NOT:
        // Out of all men in the dataset, how many took part in fraudulent transactions?
        long noFraudulentTransactions = readAllTransactions().stream()
                .filter(Transaction::isFraud)
                .count();
        long noFraudulentTransactionsByMen = readAllTransactions().stream()
                .filter(transaction -> "M".equals(transaction.getGender()))
                .filter(Transaction::isFraud)
                .count();
        return (double) noFraudulentTransactionsByMen / noFraudulentTransactions;
    }

    // task 8
    // Type signature was changed from Set<Transaction> because what is requested in the task is
    // the set of customer ids, and so there must have been an error
    public Set<String> getCustomerIdsWithNumberOfFraudulentTransactions(int numberOfFraudulentTransactions) throws Exception {
        return getCustomerIdToNumberOfTransactions().entrySet().stream()
                .filter(entry -> entry.getValue() >= numberOfFraudulentTransactions)
                .map(Map.Entry::getKey)
                .collect(Collectors.toSet());
    }

    // task 9
    public Map<String, Integer> getCustomerIdToNumberOfTransactions() throws Exception {
        return readAllTransactions().stream()
                .filter(Transaction::isFraud)
                .collect(Collectors.groupingBy(
                        Transaction::getCustomerId,
                        Collectors.collectingAndThen(
                                Collectors.counting(),
                                Long::intValue // counting collector gives Long so convert to Integer
                        )
                ));
    }

    // task 10
    public Map<String, Double> getMerchantIdToTotalAmountOfFraudulentTransactions() throws Exception {
        return readAllTransactions().stream()
                .filter(Transaction::isFraud)
                .collect(Collectors.groupingBy(
                        Transaction::getMerchantId,
                        Collectors.summingDouble(Transaction::getAmount)
                ));
    }

    // bonus
    public double getRiskOfFraudFigure(Transaction transaction) throws Exception {
        // inputs:
        // * customerId, age, gender, customerZipCode,
        // * merchantId, merchantZipCode,
        // * category, amount
        // output probability of transaction being a fraud
        // Use a TensorFlow model (through java bindings)
        // can do a more vanilla approach like logistic regression (would need a lot of experimentation with
        // parameters and adjusting for over/underfitting),
        // use a neural network, or XGBoost
        // this link seems to have helpful guidance:
        // https://medium.com/analytics-vidhya/financial-transaction-fraud-detection-6e1384169398
        // Data does not need to be balanced so no need to over/under sample
        // This could take a very long time so instead I will dedicate myself to the social good project
        return 1.0;
    }
}
