import logging
from typing import Any

# Configure logging for Jupyter
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def summarize_data(df: Any) -> None:
    """
    Print summary statistics for a DataFrame.
    :param df: pandas DataFrame
    """
    logger.info("DataFrame shape: %s", df.shape)
    display(df.head())
    display(df.describe())
