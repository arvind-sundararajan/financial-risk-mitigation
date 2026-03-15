```json
{
    "utils/data_utils.py": {
        "content": "
import logging
from typing import List, Dict
from AutoGen import StateGraph
from ultralytics import YOLO
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the mean and standard deviation of the dataset
        mean = np.mean(data)
        std_dev = np.std(data)
        
        # Calculate the non-stationary drift index
        non_stationary_drift_index = (std_dev / mean) * 100
        
        logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        return non_stationary_drift_index
    
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        return None


def stochastic_regime_switch(data: List[float], threshold: float) -> bool:
    """
    Determine if a stochastic regime switch has occurred based on the given dataset and threshold.

    Args:
    - data (List[float]): The input dataset.
    - threshold (float): The threshold value.

    Returns:
    - bool: True if a stochastic regime switch has occurred, False otherwise.
    """
    try:
        # Calculate the mean and standard deviation of the dataset
        mean = np.mean(data)
        std_dev = np.std(data)
        
        # Check if the mean is above the threshold
        if mean > threshold:
            logger.info('Stochastic regime switch detected')
            return True
        else:
            logger.info('No stochastic regime switch detected')
            return False
    
    except Exception as e:
        logger.error(f'Error detecting stochastic regime switch: {e}')
        return False


def create_state_graph() -> StateGraph:
    """
    Create a state graph using the AutoGen library.

    Returns:
    - StateGraph: The created state graph.
    """
    try:
        # Create a new state graph
        state_graph = StateGraph()
        
        # Add nodes and edges to the state graph
        state_graph.add_node('node1')
        state_graph.add_node('node2')
        state_graph.add_edge('node1', 'node2')
        
        logger.info('State graph created')
        return state_graph
    
    except Exception as e:
        logger.error(f'Error creating state graph: {e}')
        return None


def detect_anomalies(data: List[float]) -> List[float]:
    """
    Detect anomalies in the given dataset using the YOLO algorithm.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - List[float]: The detected anomalies.
    """
    try:
        # Create a YOLO model
        model = YOLO('yolov8n.yaml')
        
        # Detect anomalies in the dataset
        anomalies = model(data)
        
        logger.info('Anomalies detected')
        return anomalies
    
    except Exception as e:
        logger.error(f'Error detecting anomalies: {e}')
        return []


if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    non_stationary_drift_index = load_non_stationary_drift_index(data)
    stochastic_regime_switch_result = stochastic_regime_switch(data, 3.0)
    state_graph = create_state_graph()
    anomalies = detect_anomalies(data)
    
    logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
    logger.info(f'Stochastic regime switch: {stochastic_regime_switch_result}')
    logger.info(f'State graph: {state_graph}')
    logger.info(f'Anomalies: {anomalies}')
",
        "commit_message": "feat: implement specialized data_utils logic"
    }
}
```